import datetime
from django import forms
from django.forms import ModelForm
from app_basquetbolistas.models import Basquet

class BasquetForm(forms.Form):
    numeroDeSocio = forms.IntegerField(label='Numero de socio')
    nombre=forms.CharField(max_length=40, min_length=1, label='Nombre')
    fechaDeIngreso = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})) 
    email = forms.EmailField(label='Correo electrónico')