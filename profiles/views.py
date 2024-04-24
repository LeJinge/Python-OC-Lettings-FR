from django.shortcuts import render, get_object_or_404

from .models import Profile


def profiles_index(request):
    profiles_list = Profile.objects.all()
    return render(request, 'profiles/profiles_index.html', {'profiles_list': profiles_list})


def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'profiles/profile.html', {'profile': profile})
