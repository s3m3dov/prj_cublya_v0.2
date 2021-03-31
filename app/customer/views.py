from django.shortcuts import render



def account(request):
    return render(request, 'account.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')