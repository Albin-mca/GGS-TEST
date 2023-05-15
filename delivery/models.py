from django.db import models

class Delivery(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    status_choices = (
        ('C', 'Collected'),
        ('T', 'On transit'),
        ('S', 'Shipped'),
    )
    status = models.CharField(max_length=1, choices=status_choices, default='C')
    delivery_boy = models.ForeignKey('DeliveryBoy', on_delete=models.SET_NULL, null=True, blank=True)

# class DeliveryBoy(models.Model):
#     name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name

from django.contrib.auth.models import AbstractUser

class DeliveryBoy(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
