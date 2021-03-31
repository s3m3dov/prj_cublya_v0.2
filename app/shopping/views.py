from django.shortcuts import render, get_object_or_404

from .models import Category, Product  # Import Models

# A page shows all catgeories with their images
def categories_overview(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request, 'categories.html', context)

# Product page
def product_page(request, category_slug, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug) # Get product object
    context = {
        'product' : product,
    }
    return render(request, 'product_page.html', context)