from django.shortcuts import render


def index(request):
    """Render the homepage template."""
    return render(request, "index.html")


def cart(request):
    """Render the shopping cart page."""
    return render(request, "cart.html")


def checkout(request):
    """Render the checkout page."""
    return render(request, "checkout.html")


def product_details(request):
    """Render the product details page."""
    return render(request, "product-details.html")


def shop(request):
    """Render the shop listing page."""
    return render(request, "shop.html")
