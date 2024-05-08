"""
lettings/models.py

Ce module définit les modèles de données pour l'application lettings.
Il contient deux classes, Address et Letting, qui représentent respectivement une adresse et une location.
"""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.
class Address(models.Model):
    """
        Modèle représentant une adresse.

        Attributs :
            number (PositiveIntegerField) : Le numéro de l'adresse.
            street (CharField) : Le nom de la rue.
            city (CharField) : Le nom de la ville.
            state (CharField) : Le code de l'état.
            zip_code (PositiveIntegerField) : Le code postal.
            country_iso_code (CharField) : Le code ISO du pays.
        """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
                Options de configuration pour le modèle Address.

                Attributs :
                    verbose_name (str) : Le nom utilisé dans l'interface d'administration de Django.
                    verbose_name_plural (str) : Le nom au pluriel du modèle, utilisé dans l'interface
                    d'administration de Django.
                """
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
        Modèle représentant une location.

        Attributs :
            title (CharField) : Le titre de la location.
            address (OneToOneField) : L'adresse de la location.
        """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
