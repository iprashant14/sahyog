from rest_framework import serializers

from beneficiary.models import Beneficiary


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ('created', 'image')

    # def get_image_url(self, instance):
    #     request = self.context['request']
    #     return request.build_absolute_uri(instance.image)
