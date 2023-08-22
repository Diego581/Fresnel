from django import forms
from .models import Datos



class Inputs(forms.ModelForm):
    class Meta:
        model = Datos
        fields = '__all__'

        widgets = {
            "km" : forms.TextInput(attrs={"class": "form-control"}),
            "Ghz" : forms.TextInput(attrs={"class": "form-control"})
        }