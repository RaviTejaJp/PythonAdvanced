from django.db import models
from orders.models import Orders


# Create your models here.
class Rating(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    rating = models.IntegerField()
