from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for an individual item inside an Order."""

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product_name",
            "quantity",
            "unit_price",
            "line_total",
        )
        read_only_fields = ("id", "line_total")


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order with nested OrderItem data."""

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "status",
            "total_amount",
            "created_at",
            "updated_at",
            "items",
        )
        read_only_fields = (
            "id",
            "user",
            "total_amount",
            "created_at",
            "updated_at",
            "items",
        )
