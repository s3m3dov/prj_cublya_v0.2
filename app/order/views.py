from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Order, OrderItem


def orders_overview(request):
    # Previous Url (Get Back Url) in template
    prev_url = reverse('customer:account', args=[], kwargs={}) 

    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'orders_overview.html', context)


def order_details(request, order=None):
    prev_url = reverse('order:orders_overview', args=[], kwargs={})

    order = get_object_or_404(Order, id=order)
    order_items = OrderItem.objects.filter(order=order)

    context = {
        'prev_url' : prev_url,
        'order': order,
        'order_items': order_items,

    }
    return render(request, 'order_details.html', context)