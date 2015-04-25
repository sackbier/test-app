#from django import forms

"""class DroneForm(forms.Form):
    titel = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)"""

from django.forms import ModelForm
from .models import Drone

class DroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = ['drone_model', 'description', 'price', 'camera']