from django.db import models
from pizza.models import Pizza


# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=255)
    member_since = models.DateTimeField()
    image = models.CharField(max_length=9999, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    favorite_pizza = models.ForeignKey(Pizza, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
