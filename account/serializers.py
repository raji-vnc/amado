from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user. Handles password hashing
    and returns the essential fields after registration.
    """
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # Auto‑create an empty Profile linked to the user
        Profile.objects.get_or_create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    """Simple serializer for the Profile model.
    Add extra profile fields here as you extend the model.
    """
    class Meta:
        model = Profile
        fields = ("id", "user")
        read_only_fields = ("id", "user")
