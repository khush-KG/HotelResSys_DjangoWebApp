"""
WSGI config for Lotus_Delights_Hotels_and_Dinings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lotus_Delights_Hotels_and_Dinings.settings')

application = get_wsgi_application()
