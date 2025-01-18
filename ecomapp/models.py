from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Customer(models.Model):
#     firstname = models.CharField(max_length=20)
#     lastname = models.CharField(max_length=20)
#     middlename = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     phone = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(default="")
    price = models.FloatField()

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField()

