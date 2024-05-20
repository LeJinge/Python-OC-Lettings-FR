"""
lettings/admin.py

Ce module contient la configuration de l'interface d'administration de Django pour
l'application lettings.
Il enregistre les modèles Letting et Address pour qu'ils soient accessibles
dans l'interface d'administration de Django.
"""

from django.contrib import admin
from .models import Letting
from .models import Address

# Register your models here.

admin.site.register(Letting)
admin.site.register(Address)
