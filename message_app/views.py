import datetime

from django.shortcuts import render
from twilio.rest import Client
from whatsapp_messager.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.http import HttpResponse
import pywhatkit
import datetime


# Create your views here.

def homepage(request):
    if request.method == "POST":
        message = request.POST.get('message')
        number = request.POST.get('number')
        now = datetime.datetime.now()
        print(now.year, now.month, now.day, now.hour, now.minute, now.second)

        pywhatkit.sendwhatmsg('+91 {}'.format(number), '{}'.format(message), now.hour, now.minute + 1)

        return render(request, 'homepage.html')

    return render(request, 'homepage.html')


def twilio(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print(client)
    if request.method == "POST":
        number = request.POST.get('number')
        messages = request.POST.get('message')

        print(number, messages)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Your {} code is {}'.format("MR.", messages),
            to='whatsapp:+91{}'.format(number)
        )

        print(number)
        print(message.sid)
        print(message)
        return HttpResponse('Great! Expect a message...')
