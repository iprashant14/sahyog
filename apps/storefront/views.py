from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "storefront/home.html"

    def get_context_data(self, **kwargs):
        return {}
