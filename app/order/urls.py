from django.urls import path

from .views import orders_overview, order_details

urlpatterns = [
    path('c/my_orders/', orders_overview, name="orders_overview"),
    path('order_details/<order>/', order_details, name="order_details"),
]
