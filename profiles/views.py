from django.shortcuts import render, get_object_or_404

from .models import Profile


def profiles_index(request):
    """
    Vue pour la page d'index des profils.

    Cette vue récupère tous les profils et les passe à la template 'profiles/profiles_index.html'.

    Args :
        request (HttpRequest) : L'objet requête HTTP Django.

    Returns :
        HttpResponse : L'objet réponse HTTP Django.
    """
    profiles_list = Profile.objects.all()
    return render(request, 'profiles/profiles_index.html', {'profiles_list': profiles_list})


def profile_detail(request, profile_id):
    """
    Vue pour la page de détail d'un profil.

    Cette vue récupère le profil correspondant à l'ID donné et le passe à la template 'profiles/profile.html'.
    Si aucun profil correspondant n'est trouvé, une erreur 404 est déclenchée.

    Args :
        request (HttpRequest) : L'objet requête HTTP Django.
        profile_id (int) : L'ID du profil à afficher.

    Returns :
        HttpResponse : L'objet réponse HTTP Django.
    """
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'profiles/profile.html', {'profile': profile})
