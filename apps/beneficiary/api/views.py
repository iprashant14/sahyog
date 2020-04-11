from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from beneficiary.api import serializers
from beneficiary.models import Beneficiary
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny


class BeneficiaryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.BeneficiarySerializer
    queryset = Beneficiary.objects.all()
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('created',)
    filterset_fields = ('image_date',)

