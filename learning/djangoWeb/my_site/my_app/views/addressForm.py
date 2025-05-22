from django import forms
from my_app.models import address

class addressRegistration(forms.ModelForm):
    class Meta:
        model = address
        fields = ['city', 'state']
        widgets = {
            'city' : forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'state' : forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }