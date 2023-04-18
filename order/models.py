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
    products = models.ManyToManyField(Product)
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS, null=False, default=0)
    time_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(p.price for p in self.products.all())
    
    def __str__(self) -> str:
        return f'{self.user.username}'
