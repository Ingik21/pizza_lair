from django.forms import ModelForm, widgets

from cart.models import ContactInformation, ShippingAddress


class ContactInformationForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id', 'user_id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter your name',
                                             'aria-label': 'Enter your name',
                                             }),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Enter your phone number',
                                              'aria-label': 'Enter your phone number',}),
            'email': widgets.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Enter your email',
                                              'aria-label': 'Enter your email',}),
            'address': widgets.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Enter your address',
                                                'aria-label': 'Enter your address',}),
            'city': widgets.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter your city',
                                             'aria-label': 'Enter your city',}),
            'zipcode': widgets.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Enter your zipcode',
                                                'aria-label': 'Enter your zipcode',}),
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
