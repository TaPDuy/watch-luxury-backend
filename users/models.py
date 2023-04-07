from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from authentication.managers import UserManager

from products.models import Product
from favorite.models import Favorite


class User(AbstractBaseUser):

    # Attributes
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, blank=True)
    favorites = models.ManyToManyField(Product, through=Favorite, related_name='favorited_by')

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
