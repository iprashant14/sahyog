from rest_framework import serializers

from beneficiary.models import Beneficiary


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ('created', 'image', 'image_date')
