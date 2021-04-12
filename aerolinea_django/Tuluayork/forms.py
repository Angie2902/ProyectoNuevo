from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electronico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username':'Nombre de Usuario',
            'first_name' : 'Nombres', 
            'last_name' : 'Apellidos',   
        }
        help_texts = {k: "" for k in fields}
    

class VuelosForm(forms.ModelForm):

    class Meta:
        model = Vuelos
        fields = ['aerolinea', 'costo', 'NoCupos','fechaSalida', 'horaSalida', 'fechaLlegada', 'horaLlegada', 'LugarSalida','Destino']
        labels = {

            'fechaSalida':'Fecha de Salida',
            'fechaLlegada' : 'Fecha de Regreso', 
            'horaSalida' : 'Hora de Salida', 
            'horaLlegada':'Hora de Regreso',
            'LugarSalida' : 'Lugar de Salida', 
        }


