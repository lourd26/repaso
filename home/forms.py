from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class FormularioBusqueda(forms.Form):
    marca = forms.CharField(max_length=20,required=False)
    
class EdicionPaleta(forms.Form):
    marca = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    fecha_carga = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

class EditarPerfil(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Nombre', max_length=20)
    last_name = forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField()
    avatar = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','avatar']