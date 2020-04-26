from django.contrib import admin
from django.http import HttpResponse
from django.template.response import TemplateResponse

from sahyog_settings.forms import CommentForm


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        urls += [
            path('my_view/', self.admin_view(self.my_view))
        ]
        return urls

    def my_view(self, request):
        context = dict(
           # Include common variables for rendering the admin template.
            self.each_context(request),
            form=CommentForm(initial={'name': 'instance'}, auto_id=False)
        )
        return TemplateResponse(request, "custom_admin/sometemplate.html", context)
