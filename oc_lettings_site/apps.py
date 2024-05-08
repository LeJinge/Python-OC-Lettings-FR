from django.apps import AppConfig


class OcLettingsSiteConfig(AppConfig):
    """
    Configuration de l'application oc_lettings_site pour Django.

    Cette classe hérite de AppConfig et définit les paramètres spécifiques à l'application oc_lettings_site.

    Attributs :
        default_auto_field (str) : Le type de champ à utiliser pour les clés primaires automatiques.
        name (str) : Le nom de l'application. Il est utilisé par Django pour identifier l'application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oc_lettings_site'
