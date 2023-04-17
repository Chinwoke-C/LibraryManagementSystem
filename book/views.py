from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render
from rest_framework.decorators import api_view
from templated_mail.mail import BaseEmailMessage


# Create your views here.

def playground(request):
    try:
        message = BaseEmailMessage(
            template_name='email/hello.html',
            context={'name': "Asa"}
        )
        # message = EmailMessage('testing mail', 'this email is sent from django', '', ['canugwara99@gmail.com'])
        # message.attach_file('book/static/images/license.jpg')
        message.send(['asa@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse("email sent")
