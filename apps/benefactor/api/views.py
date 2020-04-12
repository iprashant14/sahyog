from rest_framework import viewsets, status

from benefactor.api import serializers
from benefactor.models import Benefactor
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class BenefactorViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.BenefactorSerializer
    queryset = Benefactor.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created',)

    @action(methods=['get'], detail=False,url_path="random")
    def random_benefactors(self, request,*args,**kwargs):

        querySet1 = Benefactor.objects.order_by('?').all()[:3]
        serializer = serializers.BenefactorSerializer(querySet1,many=True,context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
