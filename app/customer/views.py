from django.shortcuts import render
from django.urls import reverse


def account(request):
    prev_url = reverse('core:home', args=[], kwargs={})
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'account.html', context)

def edit_details(request):
    prev_url = reverse('customer:account', args=[], kwargs={})
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'edit_details.html', context)

# Authentication
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')