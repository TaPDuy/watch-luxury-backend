from django.db import models
from watchLuxuryAPI import settings

from products.models import Product


class Favorite(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product', )

    def __str__(self) -> str:
        return self.user.username
