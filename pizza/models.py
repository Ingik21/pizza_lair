from django.db import models


# Create your models here.
class PizzaCategory(models.Model):
    name = models.CharField(max_length=255)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, blank=True)
    base_price = models.FloatField()
    on_sale = models.BooleanField()
    offer = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class PizzaImage(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
