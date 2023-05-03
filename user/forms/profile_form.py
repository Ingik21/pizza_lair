from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'favorite_pizza': widgets.Select(attrs={'class': 'form-control'}),
            'image': widgets.Select(attrs={'class': 'form-control'})
        }