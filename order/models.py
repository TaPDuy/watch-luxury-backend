from django.db import models

from users.models import User
from products.models import Product

ORDER_STATUS = (
    (0, 'Pending'), 
    (1, 'Delivered'), 
    (2, 'Deleted')
)
ORDER_STATUS_DICT = { k: v for v, k in ORDER_STATUS }


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=300, blank=True)
    products = models.ManyToManyField(Product)
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS, null=False, default=0)
    time_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(p.price for p in self.products.all())
    
    def __str__(self) -> str:
        return f'{self.user.username}'
    
    def save(self, *args, **kwargs):
        if not self.name:
            if self.user.first_name and self.user.last_name:
                self.name = self.user.first_name + ' ' + self.user.last_name
            else:
                self.name = self.user.username
                
        if not self.phone_number:
            self.phone_number = self.user.phone_number

        if not self.address:
            self.address = self.user.address

        super().save(*args, **kwargs)
