from dataclasses import fields
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

User = get_user_model()
from .models import UserProfile

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email

        return token


class RegisterUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'location', 'phone_number')

    def create(self, validated_data):
        user = UserProfile.objects.create(**validated_data)
        return user


class RetrieveUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def get_user_profile(self, obj):
        try:
            return UserProfileSerializer(obj.profile).data
        except:
            return []


class UpdateUserSerializer(serializers.ModelSerializer):
    model = User
    fields = ('email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        for field in fields():
            if field.name in validated_data:
                setattr(instance, field.name, validated_data[field.name])
        instance.save()
        return instance