from rest_framework.routers import DefaultRouter

from benefactor.api.views import BenefactorViewSet
from beneficiary.api.views import BeneficiaryViewSet
from contact.api.views import EmailViewSet

router = DefaultRouter()
router.register('beneficiary', BeneficiaryViewSet, basename='beneficiary')
router.register('benefactor', BenefactorViewSet, basename='benefactor')
router.register('send_email',EmailViewSet,basename='email')
