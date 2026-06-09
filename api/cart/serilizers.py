from rest_framework import generics
from cart.models import CartItem
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)


    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'user']



