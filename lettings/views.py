from django.http import Http404
from django.shortcuts import render, get_object_or_404

from oc_lettings_site.settings import logger
from .models import Letting


def lettings_index(request):
    """
    Vue pour l'index des lettings.

    Cette vue récupère tous les lettings et les renvoie
    à la template 'lettings/lettings_index.html'.

    Args :
        request (HttpRequest) : L'objet requête généré par Django.

    Returns :
        HttpResponse : La réponse générée par la vue.
    """
    try:
        lettings_list = Letting.objects.all()
        return render(request, 'lettings/lettings_index.html', {'lettings_list': lettings_list})
    except Letting.DoesNotExist:
        logger.error("Aucun objet Letting ne correspond à cet ID.", exc_info=True)
        raise Http404("Aucun objet ne correspond à cet ID.")


def letting_detail(request, letting_id):
    """
    Vue pour le détail d'un letting.

    Cette vue récupère un letting spécifique en utilisant
    son ID et le renvoie à la template 'lettings/letting.html'.
    Si le letting n'existe pas, une erreur 404 est renvoyée.

    Args :
        request (HttpRequest) : L'objet requête généré par Django.
        letting_id (int) : L'ID du letting à afficher.

    Returns :
        HttpResponse : La réponse générée par la vue.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        return render(request, 'lettings/letting.html', {
            'title': letting.title,
            'address': letting.address,
        })
    except Letting.DoesNotExist:
        logger.error("Aucun objet Letting ne correspond à cet ID.", exc_info=True)
        raise Http404("Aucun objet ne correspond à cet ID.")
