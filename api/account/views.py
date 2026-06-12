from rest_framework import generics
from account.models import CustomUser
from account.serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from account.serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=RegisterSerializer

class ProfileView(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user

