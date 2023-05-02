from django.db import models


# Create your models here.
class PizzaToppings(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class MenuPizzas(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    toppings = models.ForeignKey(PizzaToppings, on_delete=models.CASCADE, blank=True)
    base_price = models.FloatField()
    on_sale = models.BooleanField()

    def __str__(self):
        return self.name


class PizzaImage(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(MenuPizzas, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
