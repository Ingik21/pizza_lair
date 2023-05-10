from django.forms import ModelForm, widgets

from cart.models import ContactInformation, ShippingAddress


class ContactInformationForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id', 'user_id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipcode': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'date_added': widgets.HiddenInput(),
            'order': widgets.HiddenInput(),
            'user': widgets.HiddenInput(),

        }


class ShippingInformationForm(ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ['id']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipcode': widgets.TextInput(attrs={'class': 'form-control'}),
        }
