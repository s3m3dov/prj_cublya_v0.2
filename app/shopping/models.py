from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import make_thumbnail

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/c/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=7,)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    actual_price = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    
    article = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='prod_imgs/')
    thumbnail = models.ImageField(upload_to='prod_thumbs/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    is_best_seller = models.BooleanField(default=False)
    is_top_sale = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.discount > 0:
            self.actual_price = self.price * (100 - self.discount) / 100
        else:
            self.actual_price = self.price
        return super().save(*args, *kwargs)
    
    def get_absolute_url(self):
        return f'/c/{self.category.slug}/{self.slug}/' 