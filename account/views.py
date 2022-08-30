from django.shortcuts import render
from rest_framework import generics

from account.models import UserProfile
from .serializers import RegisterUserSerializer, UserProfileSerializer

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterUserSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
