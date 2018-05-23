from django.urls import path
from .views import UserApi, CrimeMap, EntertainmentMap, EventMap, ArtMap, DirtinessMap
from rest_framework.authtoken import views

urlpatterns = [
    path('user/', UserApi.as_view(), name="user-detail"),
    path('login/', views.obtain_auth_token),
    path('crime/', CrimeMap.as_view(), name='crime'),
    path('entertainment/', EntertainmentMap.as_view(), name='entertainment'),
    path('events/', EventMap.as_view(), name='events'),
    path('art/', ArtMap.as_view(), name='art'),
    path('dirtiness/', DirtinessMap.as_view(), name='dirtiness'),
]