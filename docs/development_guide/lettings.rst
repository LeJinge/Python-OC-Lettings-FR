Lettings App
============

L'application Lettings gère les listings de locations.

Modèles
-------

- **Letting** : Représente un lieu de location avec des champs tels que `title` et `address`.

- **Address** : Représente une adresse avec les champs `numbers`, `street`, `city`, `state`, `zip_code` et `country`.

# Vues

- **Letting_index** : Affiche la liste des locations.
- **Letting_Detail** : Affiche les détails d'une location spécifique.

# URLS

- `/lettings/` : Affiche la liste des locations.
- `/lettings/<lettings_id>/` : Affiche les détails d'une location spécifique.
