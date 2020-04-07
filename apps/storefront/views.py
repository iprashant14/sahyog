from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from benefactor.models import Benefactor


class HomeView(TemplateView):
    template_name = "storefront/home.html"

    def get_context_data(self, **kwargs):
        benefactor_count = Benefactor.objects.count()
        benefactor_limit = 3 if benefactor_count > 3 else benefactor_count
        return {
            "total_benefactors": benefactor_limit,
            "benefactors": Benefactor.objects.order_by('created')[:benefactor_limit]
        }
