from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib import messages
from django.views.generic import CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Customer

from .forms import UserUpdateForm, CustomerUpdateForm

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

class EditDetailsView(UpdateView, UserUpdateForm, CustomerUpdateForm):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        c_form = CustomerUpdateForm(instance=request.user.customer)
        if not request.user.is_authenticated:
            return redirect('core:home')
        else:
            prev_url = reverse('customer:account')

            context = {
                'prev_url' : prev_url,
                'user_form': u_form,
                'customer_form': c_form
            }
            return render(request, 'edit_details.html', context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        c_form = UserUpdateForm(request.POST, instance=request.user.customer)

        if c_form.is_valid() and u_form.is_valid():
            u_form.save()
            c_form.save()
            messages.success(request,'Your Profile has been updated!')

            return redirect('customer:account')
        else:
            return redirect('customer:edit_details')



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