"""
profiles/apps.py

Ce module définit la configuration de l'application profiles pour Django.
Il contient une classe ProfilesConfig qui hérite de AppConfig.
Cette classe est utilisée par Django pour configurer l'application profiles.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
