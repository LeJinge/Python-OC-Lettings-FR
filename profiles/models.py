from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Modèle Profile pour l'application profiles.

    Attributs :
        user (OneToOneField) : Relation un-à-un avec le modèle User.
                           Si un User est supprimé, le Profile associé sera également supprimé.
        favorite_city (CharField) : Champ de caractères pour la ville favorite de l'utilisateur.
                                Peut être laissé vide.

    Méthodes :
        __str__ : Retourne le nom d'utilisateur de l'User associé.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Méthode pour retourner une représentation sous forme de chaîne de caractères du modèle Profile.

        Retourne :
            str : Le nom d'utilisateur de l'User associé à ce Profile.
        """
        return self.user.username
