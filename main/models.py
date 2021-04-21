from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_phone = models.CharField(max_length=30, null=False, blank=False)
    address_from = models.CharField(max_length=200, null=False, blank=False)
    address_to = models.CharField(max_length=200, null=False, blank=False)
    in_what_time = models.CharField(max_length=100, null=False, blank=False)
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, related_name='orders')
    order_done = models.BooleanField(default=False)

    def __str__(self):
        return f"Номер замовлення: {self.id} | Ім'я клієнта: {self.customer_name}"


class Car(models.Model):
    brand = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand}, {self.number}"
