from django.core.mail import EmailMessage
from rest_framework import viewsets

from contact.api import serializers
from contact.models import Email
from rest_framework.permissions import AllowAny

from sahyog_settings import settings


def send_email(receiver_email):
    email = EmailMessage(
        settings.CONTACT_US_SUBJECT_CONTENT,
        settings.CONTACT_US_MESSAGE_BODY,
        settings.CONTACT_US_SENDER_EMAIL,
        [receiver_email]
    )
    email.send()


class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.EmailSerializer
    queryset = Email.objects.all()

    def create(self, request, *args, **kwargs):
        response = super(EmailViewSet, self).create(request, *args, **kwargs)
        send_email(self.request.data.get('email'))  # sending mail
        return response

