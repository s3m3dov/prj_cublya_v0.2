from django.shortcuts import render
from django.urls import reverse

from app.shopping.models import Product


def cart(request):
    prev_url = reverse('core:home', args=[], kwargs={})

    cart_prods = Product.objects.all()[:3]  # Get random 3 product objects for testing

    context = {
        'prev_url' : prev_url,
        'cart_prods' : cart_prods,
    }
    return render(request, 'cart.html', context)


def checkout(request):
    prev_url = reverse('cart:cart', args=[], kwargs={})

    cart_prods = Product.objects.all()[:3]  # Get random 3 product objects for testing

    context = {
        'prev_url' : prev_url,
        'cart_prods' : cart_prods,
    }
    return render(request, 'checkout.html', context)