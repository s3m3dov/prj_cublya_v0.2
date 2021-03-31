from django.shortcuts import render

def orders_overview(request):
    return render(request, 'order_details.html')