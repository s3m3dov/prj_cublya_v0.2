from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import account, edit_details, settings
from .views import LoginView, register

urlpatterns = [
    path('account/', account, name="account"),
    path('account/edit_details/', edit_details, name="edit_details"),
    path('account/settings/', settings, name="settings"),

    # Authentication
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name="register"),
]