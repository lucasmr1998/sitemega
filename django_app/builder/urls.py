from django.urls import path
from . import views

app_name = 'builder'

urlpatterns = [
    path('p/<slug:slug>', views.page_view, name='page'),
]
