from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=999)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    time_added = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
