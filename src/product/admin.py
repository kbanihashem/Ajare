from django.contrib import admin
from .models import Product, Rating, Comment

admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Comment)
