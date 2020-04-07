from rest_framework.routers import DefaultRouter

from benefactor.api.views import BenefactorViewSet

router = DefaultRouter()
router.register('benefactor', BenefactorViewSet, basename='benefactor')
