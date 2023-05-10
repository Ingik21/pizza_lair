from django.forms import ModelForm, widgets
from cart.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'CVC': widgets.TextInput(attrs={'class': 'form-control'}),
            'order': widgets.HiddenInput(),
            'user': widgets.HiddenInput(),
        }