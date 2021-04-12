from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .models import *
from .forms import *
from django.contrib import messages
from .forms import UserRegisterForm
import requests


# Create your views here.

def index(request): 
    return render(request, 'Tuluayork/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            nuevo_usuario = User(
                email=form.cleaned_data.get('email'),
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                is_active= True
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            grupo = Group.objects.get(name='Cliente') 
            grupo.user_set.add(nuevo_usuario)
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado') 
            return redirect('index')       
    else:
        form = UserRegisterForm()

    context= { 'form' : form}    
    return render(request, 'Tuluayork/registro.html', context)

def profile(request):
    return render(request, 'Tuluayork/profile.html')

""""
CRUDS VUELOS 
"""
def crearVuelo(request):
    if request.method == 'POST':
        vuelo_form = VuelosForm(request.POST)
        if vuelo_form.is_valid():
            vuelo_form.save()
            return redirect('mostarVuelos')
    else:
        vuelo_form = VuelosForm()
    return render(request, 'Tuluayork/crear_vuelo.html', {'vuelo_form':vuelo_form})

def mostrarVuelos(request):
    vuelos = Vuelos.objects.filter(estado = True) 
    return render(request, 'Tuluayork/mostar_vuelos.html', {'vuelos': vuelos})

def detalleVuelos(request, id):
    vuelo = Vuelos.objects.filter(id = id) 
    return render(request, 'Tuluayork/detalleVuelos.html', {'vuelo': vuelo})

def editarVuelo(request, id):
    vuelo_form  = None
    error = None
    try:
        vuelo = Vuelos.objects.get(id = id)
        if request.method == 'GET':
            vuelo_form = VuelosForm(instance = vuelo)
        else:
            vuelo_form = VuelosForm(request.POST, instance = vuelo)
            if vuelo_form.is_valid():
                vuelo_form.save()
            return redirect('mostarVuelos')
    
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'Tuluayork/crear_vuelo.html', {'vuelo_form': vuelo_form, 'error': error})

def EliminarVuelo(request, id):
    vuelo = Vuelos.objects.get(id=id)
    if request.method == 'POST':
        vuelo.estado = False
        vuelo.save()
        return redirect('mostarVuelos')
    return render(request, 'Tuluayork/eliminar_vuelo.html', {'vuelo':vuelo})

def mostrarVuelosAbril(request):

    fecha_inicio = '01/04/2021'
    fecha_final = '30/04/2021'

    d_fecha_inicio = datetime.strptime(fecha_inicio,'%d/%m/%Y')
    d_fecha_final = datetime.strptime(fecha_final,'%d/%m/%Y') 

    vuelos=Vuelos.objects.filter(fechaSalida__range=(d_fecha_inicio,d_fecha_final))
     
    return render(request, 'Tuluayork/mostar_vuelos.html', {'vuelos': vuelos})


""""
CRUDS USUARIOS 
"""
"""
def crearUsuario(request):
    if request.method == 'POST':
        vuelo_form = VuelosForm(request.POST)
        if vuelo_form.is_valid():
            vuelo_form.save()
            return redirect('index')
    else:
        vuelo_form = VuelosForm()
    return render(request, 'Tuluayork/crear_vuelo.html', {'vuelo_form':vuelo_form})
"""

def mostrarUsuario(request):
    usuario = User.objects.filter(is_active = True) 
    return render(request, 'Tuluayork/mostar_usuario.html', {'usuario': usuario})

def editarUsuario(request, Username):

    form  = None
    error = None

    try:
        usuario = Vuelos.objects.get(Username = Username)
        if request.method == 'GET':
            form = UserRegisterForm(instance = usuario)
        else:
            form = UserRegisterForm(request.POST, instance = usuario)
            if form.is_valid():
                form.save()
            return redirect('mostarUsuario')
    
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'Tuluayork/registro.html', {'form': form, 'error': error})

def EliminarUsuario(request, Username):
    usuario = User.objects.get(Username=Username)
    if request.method == 'POST':
        usuario.is_active = False
        usuario.save()
        return redirect('mostarUsuario')
    return render(request, 'Tuluayork/eliminar_usuario.html', {'usuario':usuario})


""""
CRUDS RESERVAS 
"""


def crearReserva(request, idVuelo):
    
    hoy = datetime.datatime.now()
    reserva = User(fechaHoraReserva = hoy)  
    reserva.save()        
    usuario = User.objects.get(Username=Username)
    usuario.user_set.add(reserva)
    vuelo = Vuelos.objects.get(id=idVuelo)
    vuelov.vuelo_set.add(reserva)
    
    return render(request, 'Tuluayork/crear_reserva.html', {'reserva':reserva})

  
def mostrarReservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'Tuluayork/mostar_reserva.html', {'reservas': reservas})
 


def EliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    if request.method == 'POST':
        reserva.is_active = False
        reserva.save()
        return redirect('mostrarReservas')
    return render(request, 'Tuluayork/eliminar_reserva.html', {'reserva':reserva})




"""
API 
"""

def indexApi(request):
    api_url = "http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    
    #vuelo = Vuelos.objects.get(id = id)
    ciudad1 = "Tuluá"

    
  

    url = api_url + str(ciudad1) 

    response = requests.get(url)
    content = response.json()
    weather_data = []
    
    city_weather = {
        'city' : ciudad1,
        'temperature' : content['main']['temp'],
        'description': content['weather'][0]['description'],
        'icon' : content['weather'][0]['icon'],

    }
    weather_data.append(city_weather)
    return render(request, 'Tuluayork/weather.html', {'weather_data': weather_data})

