from rest_framework import serializers
from django.contrib.auth.models import User
from django.urls import path
from .views import RegisterViewSet, ProfileViewSet, profile, register, login

urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('profile/', profile, name='profile'),  
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/update/', ProfileViewSet.as_view({'put': 'update'}), name='profile-update'),
]