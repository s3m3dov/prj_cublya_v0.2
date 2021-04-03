from django.db import models
from django.contrib.auth.models import User


# For One Vendor Ecommerce (Customer & Admin)
class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

# Assign customer model to user
User.customer = property(lambda u:Customer.objects.get_or_create(user=u)[0])