from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(default='default.jpeg', upload_to='product_pics')
    description = models.TextField()
    price = models.IntegerField(default=0) #in 1000 Tomans

    def get_rating(self):
        ratings = Rating.objects.filter(product = self)
        count = len(ratings)
        if count == 0:
            return '?'
        score = 0
        for r in ratings:
            score += r.value
        score /= count
        score = int(score * 10) / 10
        return score


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.SmallIntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

