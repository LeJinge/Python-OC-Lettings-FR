"""
oc_lettings_site/wsgi.py

Ce module configure l'application WSGI pour le projet oc_lettings_site.
Il définit l'application WSGI par défaut pour ce projet.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
