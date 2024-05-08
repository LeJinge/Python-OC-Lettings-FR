"""
Vue pour le détail d'un letting.

Cette vue récupère un letting spécifique en utilisant son ID et le renvoie à la template 'lettings/letting.html'.
Si le letting n'existe pas, une erreur 404 est renvoyée.

Args :
    request (HttpRequest) : L'objet requête généré par Django.
    letting_id (int) : L'ID du letting à afficher.

Returns :
    HttpResponse : La réponse générée par la vue.
"""

from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    # URL pour la page d'index des lettings
    path('', views.lettings_index, name='lettings_index'),

    # URL pour la page de détail d'un letting
    path('<int:letting_id>/', views.letting_detail, name='lettings_detail'),
]
