from rest_framework import viewsets

from beneficiary.api import serializers
from beneficiary.models import Beneficiary
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny


class BeneficiaryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.BeneficiarySerializer
    queryset = Beneficiary.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created',)
