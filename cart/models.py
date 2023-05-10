from django.db import models
from django_countries.fields import CountryField
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

from pizza.models import Pizza
from user.models import Profile
from offer.models import Offer

from django import forms


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        orderitemsoffers = self.orderitemoffer_set.all()
        total += sum([item.get_total for item in orderitemsoffers])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        orderitemsoffers = self.orderitemoffer_set.all()
        total += sum([item.quantity for item in orderitemsoffers])
        return total

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.pizza.base_price * self.quantity
        return total

    @property
    def get_items(self):
        total = self.quantity
        return total



class OrderItemOffer(models.Model):

    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.offer.offer_price * self.quantity
        return total

    @property
    def get_items(self):
        total = self.quantity
        return total

    @property
    def get_total(self):
        total = self.offer.offer_price * self.quantity
        return total

    @property
    def get_items(self):
        total = self.quantity
        return total




class ContactInformation(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    country = CountryField()
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)


class Payment(models.Model):
    cardholder_name = models.TextField(max_length=200)
    card_number = CardNumberField()
    expiration_date = CardExpiryField()
    CVC = SecurityCodeField()


class ShippingAddress(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)



class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['name', 'email', 'phone_number']
