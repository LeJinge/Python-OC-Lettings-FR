"""
lettings/apps.py

Ce module définit la configuration de l'application lettings pour Django.
Il contient une classe LettingsConfig qui hérite de AppConfig.
Cette classe est utilisée par Django pour configurer l'application lettings.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
        Configuration de l'application lettings pour Django.

        Attributs :
            name (str) : Le nom de l'application. Il est utilisé par Django pour identifier l'application.
        """
    name = 'lettings'
