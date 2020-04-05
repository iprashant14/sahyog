"""
WSGI config for sahyog_settings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import sys
from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sahyog_settings.settings')

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

application = get_wsgi_application()