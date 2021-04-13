from django.shortcuts import render

from app.shopping.models import Product

def home(request):
    bs_prods = Product.objects.filter(is_best_seller=True) # Best Seller Products
    ts_prods = Product.objects.filter(is_top_sale=True) # Top Sale Products

    context = {
        'bs_prods' : bs_prods,
        'ts_prods' : ts_prods
    }
    return render(request, 'index.html', context)