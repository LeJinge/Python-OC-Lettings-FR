from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, trigger_500

handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'

urlpatterns = [
    path('trigger-500/', trigger_500, name='trigger-500'),
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
