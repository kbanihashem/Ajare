from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_tomans = models.IntegerField(default=0)

class Order(models.Model):
    STATUS_PAID = 'Paid'
    STATUS_RETURNED = 'Returned'
    STATUSES = (
        (STATUS_PAID, STATUS_PAID),
        (STATUS_RETURNED, STATUS_RETURNED)
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUSES)
    
    return_date = models.DateField(null=True, blank=True)
    damage_cost_tomans = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"User <{self.user.username}>  Product<{self.product_id}>"
