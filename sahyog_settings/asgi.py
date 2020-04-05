"""
ASGI config for sahyog_settings project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sahyog_settings.settings')

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

application = get_asgi_application()
