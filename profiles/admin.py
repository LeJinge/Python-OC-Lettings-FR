"""
profiles/admin.py

Ce module contient la configuration de l'interface d'administration
de Django pour l'application profiles.
Il enregistre le modèle Profile pour qu'il soit accessible
dans l'interface d'administration de Django.
"""

from django.contrib import admin

# Register your models here.
from .models import Profile

admin.site.register(Profile)
