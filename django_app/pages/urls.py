from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('energia', views.energia, name='energia'),
    path('rastreamento', views.rastreamento, name='rastreamento'),
    path('algar', views.algar, name='algar'),
    path('lojas', views.lojas, name='lojas'),
]
