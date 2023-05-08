from django.db import models

from pizza.models import Pizza
from user.models import Profile


# Create your models here.







class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    #todo get_cart_total
    #todo get_cart_items

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
