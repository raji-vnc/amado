from django.shortcuts import render


def index(request):
    """Render the homepage template."""
    return render(request, "index.html")
