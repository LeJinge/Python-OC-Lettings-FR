from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)


def trigger_500(request):
    raise Exception("Ceci est une erreur délibérée pour tester la gestion des erreurs 500.")
