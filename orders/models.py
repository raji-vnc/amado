from django.conf import settings
from django.db import models
from stripe import Price


class ShippingAddress(models.Model):
    user=models.ForeignKey('account.CustomUser',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=20)
    address=models.TextField()
    is_default=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=["-created_at"]
        verbose_name="Shipping Address"
        verbose_name_plural="Shipping Addresses"
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.address}"

class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('processing','Processing'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
        ]
    user=models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    shipping_address=models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]
        verbose_name="Order"
        verbose_name_plural="Orders"
    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.status}"



class OrderItem(models.Model):
    order=models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product=models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
       ordering=["-id"]
       verbose_name="Order Item"
       verbose_name_plural="Order Items"
    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.price}"

    
 
class Payment(models.Model):

    PAYMENT_METHODS = (
        ('COD', 'Cash on Delivery'),
        ('RAZORPAY', 'Razorpay'),
        ('STRIPE', 'Stripe'),
    )

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='payment'
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )

    transaction_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.payment_method}"