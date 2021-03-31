from django.urls import path

from .views import orders_overview

urlpatterns = [
    path('my_orders/', orders_overview, name="orders_overview"),
]