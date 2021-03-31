from django.urls import path

from .views import account, login, register

urlpatterns = [
    path('account/', account, name="account"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]