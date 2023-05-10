from django.forms import ModelForm, widgets
from cart.models import Payment
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField



class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': CardNumberField(label='Card Number', min_length=16, max_length=16).hidden_widget.is_required,
            'expiration_date': CardExpiryField(label='Expiration Date'),
            'CVC': SecurityCodeField(label='CVC/CVV', min_length=3, max_length=3).hidden_widget.is_required,
            'order': widgets.HiddenInput(),
            'user': widgets.HiddenInput(),
        }