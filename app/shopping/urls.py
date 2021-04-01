from django.urls import path

# Import Views
from .views import categories_overview, product_page, search

urlpatterns = [
    path('categories/', categories_overview, name="categories_overview"),
    path('search/', search, name="search"),
    path('<slug:category_slug>/<slug:prod_slug>/', product_page, name="product_page"),
]