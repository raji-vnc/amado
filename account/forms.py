from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    A custom form for creating new users, extending Django's built-in UserCreationForm.
    This form includes additional fields defined in the CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "password1", "password2")
        