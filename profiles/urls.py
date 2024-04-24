from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profiles_index, name='index'),
    path('<int:profile_id>/', views.profile_detail, name='detail'),
]
