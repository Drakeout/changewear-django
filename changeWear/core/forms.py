from django.db import models
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import model_to_dict
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['apellido_paterno', 'apellido_materno','telefono']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class DireeccionForm(forms.ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = ['direccion', 'region', 'comuna']

class EmpleoForm(forms.ModelForm):
    class Meta:
        model = DataEmpleo
        fields = '__all__'

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactanos
        fields = '__all__'
