from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True,unique=True)
    profile_image=models.ImageField(upload_to='profile_images/', blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
