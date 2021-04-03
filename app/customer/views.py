from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

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

@login_required()
def settings(request):
    prev_url = reverse('customer:account', args=[], kwargs={})
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'settings.html', context)

# Authentication

class LoginView(AuthLoginView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('customer:account')
        else:
            return render(request, 'login.html')

    def post(self, request):
        id_email = request.POST.get('id_email')
        password = request.POST.get('password')
        # Check if username is correct
        if not User.objects.filter(username=id_email).exists() and not User.objects.filter(email=id_email).exists():
            messages.error(request, "The username or email doesn't match any account.")
            return redirect('customer:login')
        else:
            try:
                user = authenticate(request, username=id_email, password=password)
                if user.is_active:
                    auth_login(request, user)
                    return redirect('core:home')
            except:
                messages.error(request, "The password is incorrect.")
                return redirect('customer:login')

"""def logout(request):
    auth_logout(request)
    return redirect('users:login')"""

def register(request):
    return render(request, 'register.html')