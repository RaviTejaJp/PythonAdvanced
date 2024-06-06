from django.db import models



class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)
    price_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)

    def __str__(self):
        return self.name
