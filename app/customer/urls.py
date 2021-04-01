from django.urls import path

from .views import account, edit_details, login, register

urlpatterns = [
    path('account/', account, name="account"),
    path('edit_details/', edit_details, name="edit_details"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]