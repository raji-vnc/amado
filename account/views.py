from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser, Profile, UserRegistrationAPIView
from .serializers import UserRegistrationSerializer, ProfileSerializer

# Simple view to render a placeholder template (optional)
def account_home(request):
    """Render a basic account home page (can be customized later)."""
    return render(request, "account/home.html")

# API view for user registration (re-export for convenience)
class RegisterUser(UserRegistrationAPIView):
    """Inherit the registration logic defined in models.py."""
    pass

# API view to retrieve and update user profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Allow users to retrieve and update their profile information."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "user__id"
    def get_object(self):
        return self.request.user.profile
