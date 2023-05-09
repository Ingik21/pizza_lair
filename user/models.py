
from django.contrib.auth.models import User
from django.db import models
from pizza.models import Pizza


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=9999, blank=True, null=True)


