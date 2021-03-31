from django.contrib import admin

from .models import Category, Product

# Registering
admin.site.register(Category)
admin.site.register(Product)
