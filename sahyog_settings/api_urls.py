from rest_framework.routers import DefaultRouter

from benefactor.api.views import BenefactorViewSet
from beneficiary.api.views import BeneficiaryViewSet

router = DefaultRouter()
router.register('beneficiary', BeneficiaryViewSet, basename='beneficiary')
router.register('benefactor', BenefactorViewSet, basename='benefactor')

