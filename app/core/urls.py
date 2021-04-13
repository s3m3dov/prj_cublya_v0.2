from django.urls import path
from .views import home
urlpatterns = [
    path('', home, name="home"),

]
"""path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),"""