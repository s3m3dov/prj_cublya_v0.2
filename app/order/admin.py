from django.contrib import admin

from .models import AddressInfo, Order, OrderItem

admin.site.register(AddressInfo)
admin.site.register(Order)
admin.site.register(OrderItem)
