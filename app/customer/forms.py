from django import forms
from django.contrib.auth.models import User
from .models import Customer

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'email']

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['date_of_birth','gender']
    