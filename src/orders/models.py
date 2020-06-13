from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_tomans = models.IntegerField(default=0)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.IntegerField()
    price = models.IntegerField()
    status = models.TextField()
