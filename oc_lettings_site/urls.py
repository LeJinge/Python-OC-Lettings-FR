"""
oc_lettings_site/urls.py

Ce module définit les URL pour le projet oc_lettings_site. Il comprend plusieurs routes :
- Une pour déclencher une erreur 500, utilisée uniquement pour les tests.
- Une pour la page d'administration de Django.
- Une pour la page d'accueil.
- Deux pour inclure les URL des applications lettings et profiles.

Chaque URL est associée à une vue qui est appelée lorsque l'URL est visitée.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from .views import index, trigger_500

# Handlers pour les erreurs 404 et 500
handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'

urlpatterns = [
    # URL pour déclencher une erreur 500, utilisée uniquement pour les tests
    path('trigger-500/', trigger_500, name='trigger-500'),

    # URL pour la page d'administration de Django
    path('admin/', admin.site.urls),

    # URL pour la page d'accueil
    path('', index, name='home'),

    # URL pour inclure les URL de l'application lettings
    path('lettings/', include('lettings.urls', namespace='lettings')),

    # URL pour inclure les URL de l'application profiles
    path('profiles/', include('profiles.urls', namespace='profiles')),
]

# Si le mode DEBUG est désactivé, ajoute les URL pour servir les fichiers statiques
# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]