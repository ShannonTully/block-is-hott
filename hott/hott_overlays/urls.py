from django.shortcuts import render
from django.urls import path
from .views import CrimeView, EntertainmentView, EventView, ArtView, DirtinessView



urlpatterns = [
    path('crime/', CrimeView.as_view(), name='crime'),
    path('entertainment/', EntertainmentView.as_view(), name='entertainment'),
    path('events/', EventView.as_view(), name='events'),
    path('art/', ArtView.as_view(), name='art'),
    path('complaints/', DirtinessView.as_view(), name='dirtiness'),
]