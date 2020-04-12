from rest_framework import serializers

from contact.models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('name', 'comments','email','created')
