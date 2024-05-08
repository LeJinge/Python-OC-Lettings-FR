"""
Module de configuration des URL pour l'application profiles.

Ce module définit les URL pour l'application profiles. Il comprend deux routes :
- Une pour la page d'index des profils.
- Une pour la page de détail d'un profil.

Chaque URL est associée à une vue qui est appelée lorsque l'URL est visitée.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    # URL pour la page d'index des profils
    path('', views.profiles_index, name='profiles_index'),

    # URL pour la page de détail d'un profil
    path('<int:profile_id>/', views.profile_detail, name='profile_detail'),
]
