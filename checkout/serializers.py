from rest_framework import serializers
from .models import CheckoutSession


class CheckoutSessionSerializer(serializers.ModelSerializer):
    """Serializer for a checkout session, exposing all fields."""

    class Meta:
        model = CheckoutSession
        fields = "__all__"
