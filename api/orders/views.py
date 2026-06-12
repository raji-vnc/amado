from rest_framework import generics
from orders.models import ShippingAddress,Order,OrderItem,Payment
from orders.serializers import OrderSerializer,ShippingAddressSerializer,PaymentSerializer

class ShippingAddressListView(
    generics.ListCreateAPIView
):
    serializer_class=ShippingAddressSerializer

    def get_queryset(self):
        return ShippingAddress.objects.filter(
            user=self.request.user
        )

class OrderListView(generics.ListAPIView):
    serializer_class=OrderSerializer()

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

class PaymentListView(generics.ListAPIView):
    
    queryset = Payment.objects.all()

    serializer_class = PaymentSerializer

