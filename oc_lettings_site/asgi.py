"""
oc_lettings_site/asgi.py

Ce module configure l'application ASGI pour le projet oc_lettings_site.
Il définit l'application ASGI par défaut pour ce projet.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
