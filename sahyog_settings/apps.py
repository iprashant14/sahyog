from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = 'sahyog_settings.admin.CustomAdminSite'
