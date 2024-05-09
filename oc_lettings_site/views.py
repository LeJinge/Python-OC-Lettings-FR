from django.shortcuts import render

from oc_lettings_site.settings import logger


def index(request):
    """
    Vue pour la page d'accueil.

    Cette fonction prend en argument une requête HTTP et renvoie une réponse HTTP qui affiche la page d'accueil.

    Args :
        request (HttpRequest) : La requête HTTP.

    Returns :
        HttpResponse : La réponse HTTP.
    """
    return render(request, 'index.html')


def error_404(request, exception):
    """
    Vue pour la page d'erreur 404.

    Cette fonction prend en argument une requête HTTP et une exception, et renvoie une réponse HTTP qui affiche la page d'erreur 404.

    Args :
        request (HttpRequest) : La requête HTTP.
        exception (Exception) : L'exception qui a déclenché l'erreur 404.

    Returns :
        HttpResponse : La réponse HTTP.
    """
    logger.error(f"Erreur 404 survenue : {exception}", exc_info=True)
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Vue pour la page d'erreur 500.

    Cette fonction prend en argument une requête HTTP et renvoie une réponse HTTP qui affiche la page d'erreur 500.

    Args :
        request (HttpRequest) : La requête HTTP.

    Returns :
        HttpResponse : La réponse HTTP.
    """
    logger.error("Erreur 500 survenue", exc_info=True)
    return render(request, '500.html', status=500)


def trigger_500(request):
    """
    Vue pour déclencher une erreur 500.

    Cette fonction prend en argument une requête HTTP et déclenche une exception pour tester la gestion des erreurs 500.

    Args :
        request (HttpRequest) : La requête HTTP.

    Raises :
        Exception : Une exception délibérée pour tester la gestion des erreurs 500.
    """
    raise Exception("Ceci est une erreur délibérée pour tester la gestion des erreurs 500.")
