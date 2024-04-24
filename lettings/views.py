from django.shortcuts import render, get_object_or_404
from .models import Letting


def lettings_index(request):
    lettings_list = Letting.objects.all()
    return render(request, 'lettings/lettings_index.html', {'lettings_list': lettings_list})


def letting_detail(request, letting_id):
    letting = get_object_or_404(Letting, id=letting_id)
    return render(request, 'lettings/letting.html', {
        'title': letting.title,
        'address': letting.address,
    })
