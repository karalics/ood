from django import forms
from .models import OODBeispiel 

class SatzForm(forms.Form):
    bspsatz = forms.CharField(label='Satz eingeben', max_length=100)

