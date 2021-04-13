from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import account, settings, EditDetailsView, LoginView, RegisterView

urlpatterns = [
    path('account/', account, name="account"),
    path('account/settings/', settings, name="settings"),
    path('account/edit_details/', EditDetailsView.as_view(), name="edit_details"),

    # Authentication
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
]