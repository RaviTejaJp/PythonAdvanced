from django.db import models
from orders.models import Orders


# Create your models here.
class Transactions(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.BooleanField(null=True)
