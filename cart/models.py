from django.db import models
from django.conf import settings



class Wishlist(models.Model):
    user=models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='wishlist')
    product=models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='wishlisted_by')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
        verbose_name="Wishlist Item"
        verbose_name_plural="Wishlist Items"
    def __str__(self):
        return f"{self.user.username} wishes for {self.product.name}"
# Create your models here.


class Cart(models.Model):
     user = models.OneToOneField( 'account.CustomUser',on_delete=models.CASCADE)    
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
        ordering = ["-created_at"]
        verbose_name="Cart"
        verbose_name_plural="Carts"

        def __str__(self):
         return f"Cart for {self.user.username}"


  

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    @property
    def subtotal(self):
        return self.quantity * self.product.price
    class Meta:
        ordering=["-created_at"]
        verbose_name="Cart Item"
        verbose_name_plural="Cart Items"

        def __str__(self):
         return f"{self.quantity} of {self.product.name} in cart for {self.cart.user.username}"

   