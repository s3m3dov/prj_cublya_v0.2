from django.urls import path

# Import Views
from .views import categories_overview, product_page, category_products, search

urlpatterns = [
    path('categories/', categories_overview, name="categories_overview"),
    path('search/', search, name="search"),
    path('<slug:category_slug>/products/', category_products, name="category_products"),
    path('<slug:category_slug>/product/<slug:prod_slug>/', product_page, name="product_page"),
]