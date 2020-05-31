from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(default='default.jpeg', upload_to='product_pics')
    description = models.TextField()
    price = models.IntegerField(default=0) #in 1000 Tomans
