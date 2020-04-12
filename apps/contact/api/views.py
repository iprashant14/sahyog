from django.core.mail import EmailMessage
from rest_framework import viewsets

from contact.api import serializers
from contact.models import Email
from rest_framework.permissions import AllowAny

from sahyog_settings import settings

def send_email(receiver_email):
    print(receiver_email)
    email = EmailMessage(
        settings.SUBJECT_CONTENT,
        settings.MESSAGE_BODY,
        settings.SENDER_EMAIL,
        [receiver_email]
    )
    email.send()

class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.EmailSerializer
    queryset = Email.objects.all()

    def create(self, request, *args, **kwargs):
        response = super(EmailViewSet, self).create(request, *args, **kwargs)
        send_email(self.request.POST.get("email"))  # sending mail
        return response

