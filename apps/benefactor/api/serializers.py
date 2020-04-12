from rest_framework import serializers

from benefactor.models import Benefactor


class BenefactorSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Benefactor
        fields = ('id', 'name','description', 'thumbnail_url', 'created')

    def get_thumbnail_url(self, instance):
        request = self.context['request']
        return request.build_absolute_uri(instance.thumbnail_url)
