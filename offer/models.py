from django.db import models


# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=255)
    offer_image = models.CharField(max_length=9999, blank=True)
    offer_price = models.FloatField()

    def __str__(self):
        return self.name
