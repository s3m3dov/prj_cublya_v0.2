from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import authenticate, login as auth_login


# Customer Views
@login_required()
def account(request):
    prev_url = reverse('core:home')
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'account.html', context)

@login_required()
def settings(request):
    prev_url = reverse('customer:account')
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'settings.html', context)

@login_required()
def edit_details(request):
    prev_url = reverse('customer:account')
    context = {
        'prev_url' : prev_url,
    }
    return render(request, 'edit_details.html', context)




# * Authentication *
# Login
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


# Register
class RegisterView(CreateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('customer:account')
        else:
            return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "The username already exists.")
            return redirect('customer:register')

        elif User.objects.filter(email=email).exists():
            messages.error(request, "The email address already exists.")
            return redirect('customer:register')

        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            auth_login(request, user)
            return redirect('core:home')