from django.db import models


# Create your models here.
class PizzaToppings(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()


class MenuPizzas(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    toppings = models.ForeignKey(PizzaToppings, on_delete=models.CASCADE)
    base_price = models.FloatField()
    on_sale = models.BooleanField()


class PizzaImage(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(MenuPizzas, on_delete=models.CASCADE)
