from django.db import models
from django_resized import ResizedImageField


# Create your models here.

class Product(models.Model):
    # id = primaryKey (django makes the pk column by default)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='products', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.name
