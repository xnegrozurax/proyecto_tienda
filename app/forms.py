from django import forms
from django.forms import ModelForm
from .models import * 

#CREAMOS TEMPLATES DE LOS FORMULARIOS

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=6,max_length=25)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['codigo','nombre','precio','stock','tipo','imagen',]
        
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario','contraseña','correo',]        