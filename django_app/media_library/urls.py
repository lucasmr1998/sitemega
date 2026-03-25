from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('upload', views.media_upload, name='media_upload'),
    path('<int:pk>/excluir', views.media_delete, name='media_delete'),
    path('browse', views.media_browse, name='media_browse'),
]
