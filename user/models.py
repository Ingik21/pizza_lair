from django.db import models
from pizza.models import MenuPizzas


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    member_since = models.DateTimeField()
    image = models.CharField(max_length=9999, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    favorite_pizza = models.ForeignKey(MenuPizzas, on_delete=models.RESTRICT)
