from rest_framework import viewsets

from benefactor.api import serializers
from benefactor.models import Benefactor
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny


class BenefactorViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.BenefactorSerializer
    queryset = Benefactor.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created',)
