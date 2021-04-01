from django.shortcuts import render
from django.urls import reverse

def orders_overview(request):
    prev_url = reverse('customer:account', args=[], kwargs={})
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'orders_overview.html', context)

def order_details(request):
    prev_url = reverse('order:orders_overview', args=[], kwargs={})
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'order_details.html', context)