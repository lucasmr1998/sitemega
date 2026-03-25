from django.urls import path
from . import views

urlpatterns = [
    path('lead/submit/', views.submit_lead, name='submit_lead'),
]
