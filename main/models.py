from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(blank=False, max_length=30)


class Order(models.Model):
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_phone = models.CharField(max_length=30, null=False, blank=False)
    address_from = models.CharField(max_length=200, null=False, blank=False)
    address_to = models.CharField(max_length=200, null=False, blank=False)
    in_what_time = models.CharField(max_length=100, null=False, blank=False)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='orders')
    order_done = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name


class Car(models.Model):
    brand = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.brand
