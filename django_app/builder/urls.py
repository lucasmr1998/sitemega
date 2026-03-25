from django.urls import path
from . import views

app_name = 'builder'

urlpatterns = [
    path('p/<slug:slug>', views.page_view, name='page'),
    path('lojas', views.lojas_redirect, name='lojas'),
    path('', views.page_view, name='homepage'),
]
