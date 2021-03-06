from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Category, Product  # Import Models

# A page shows all catgeories with their images
def categories_overview(request):
    categories = Category.objects.all()
    pop_prods = Product.objects.filter(is_popular=True) # Popular Products
    tr_srcs = ['Men Sweatshirt', 'Women Sweatshirt', 'Beauty Product', 'Wallet', 'CPU'] # Trending Searches

    context = {
        'pop_prods' : pop_prods,
        'tr_srcs' : tr_srcs,
        'categories' : categories,
    }
    return render(request, 'categories.html', context)


# Product page
def product_page(request, category_slug, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug) # Get product object
    sim_prods = Product.objects.exclude(slug=prod_slug)[:3] # Get 3 random products for testing | You Might Also Like

    context = {
        'product' : product,
        'sim_prods' : sim_prods,
    }
    return render(request, 'product_page.html', context)


# Category Products Page
def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    category_products = category.products.all() 
    context = {
        'category': category,
        'category_products': category_products
    }
    return render(request, 'category_products.html', context)


# Search
def search(request):
    query = request.GET.get('query')
    # instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    # Retrieve Products if title/description/article matches with search term
    src_products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(brand__icontains=query) | 
            Q(description__icontains=query) | 
            # Article
            Q(article__icontains=query)
        ).filter(actual_price__gte=price_from
        ).filter(actual_price__lte=price_to)
    # Retieve Products if instock checked (Advanced Search)
    #if instock:
    #   products = products.filter(num_available__gte=1)
    
    # Context for template
    context = {
        'query': query,    # Query (Searched Word)
        'src_products': src_products.order_by(sorting), # Products matches with query
        # Filter
        #'instock': instock, 
        # Sorting
        'price_from': price_from, 
        'price_to': price_to,
        'sorting': sorting
    }
    # return
    return render(request, 'search.html', context)