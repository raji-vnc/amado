from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name=models.CharField(max_length=255, unique=True)
    slug=models.SlugField(max_length=255, unique=True, blank=True)
    image=models.ImageField(upload_to='category_images/', blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]
        verbose_name="Category"
        verbose_name_plural="Categories"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)


class Brand(models.Model):
    name=models.CharField(max_length=255, unique=True)
    logo=models.ImageField(upload_to='brand_logos/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
        verbose_name="Brand"
        verbose_name_plural="Brands"
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand=models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    sku=models.CharField(max_length=100, unique=True)
    color=models.CharField(max_length=50, blank=True)
    material=models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Auto‑generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image=models.ImageField(upload_to='product_images/')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]
        verbose_name="Product Image"
        verbose_name_plural="Product Images"
    def __str__(self):
        return f"Image for {self.product.name}"

class Review(models.Model):
    user=models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='reviews')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating=models.IntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]
        verbose_name="Review"
        verbose_name_plural="Reviews"
    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"