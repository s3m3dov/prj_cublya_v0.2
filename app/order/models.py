from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

from app.shopping.models import Product


# Address Models
class AddressInfo(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.SET_NULL, blank=True, null=True)
    # assign address info to order model if user is authenticated

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)

    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    #class Meta:
        #verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.city} {self.country}"



# * Order Model * 
class Order(models.Model):
    # assign user info to order model if user is authenticated
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    address_info = models.ForeignKey(AddressInfo, related_name='address_info', on_delete=models.SET_NULL, blank=True, null=True) # assign address

    ordered_date = models.DateTimeField(auto_now_add=True)
    shipped_date = models.DateTimeField(blank=True, null=True)

    # STATUS_CHOICES = ['ordered', 'packing', 'shipping', 'arriving', 'success']
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ordered')

    def __str__(self):
        return f"{self.id} | {self.address_info}"
    
    def get_absolute_path(self):
        return f'/order_details/{self.id}/' 

    # Quantity of all Order Items
    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())
    
    # Total Price of all Order Items
    def get_total_price(self):
        return sum(float(item.actual_price) for item in self.items.all())
    
    # Subtotal Price of all Order Items
    def get_subtotal_price(self):
        return sum(float(item.price) for item in self.items.all())

    # Discount of all Order Items
    def get_discount(self):
        return sum(float(item.price_off) for item in self.items.all())



# * Order Item *
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)

    quantity = models.IntegerField(default=1)
    actual_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    price_off = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)

    def __str__(self):
        return f"{self.order.id} - {self.product.title}"

    def save(self, *args, **kwargs):
        self.actual_price = self.product.actual_price * self.quantity
        self.price = self.product.price * self.quantity
        self.price_off = self.price - self.actual_price 
        return super().save(*args, *kwargs)


# Delivery Model (Multivendor)