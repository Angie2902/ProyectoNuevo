from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    maxReserva = models.IntegerField(default= 2)
 

    def __str__(self):
        return f'{self.user}'

class Vuelos(models.Model):
    id = models.AutoField(primary_key=True)
    aerolinea = models.CharField(max_length= 200, blank= False, null= False)
    costo = models.IntegerField(blank= False, null= False)
    NoCupos = models.IntegerField(blank= False, null= False)
    fechaSalida = models.DateField(max_length= 200, blank= False, null= False)
    fechaLlegada = models.DateField(max_length= 200, blank= False, null= False)
    horaSalida = models.TimeField(max_length= 200, blank= False, null= False)
    horaLlegada = models.TimeField(max_length= 200, blank= False, null= False)
    LugarSalida = models.CharField(max_length= 200, blank= False, null= False)
    Destino = models.CharField(max_length= 200, blank= False, null= False)
    Requisitos = models.TextField(max_length= 200, blank= False, null= False, default= 'COVID 19')
    InfoAdicional = models.TextField(max_length= 200, blank= False, null= False, default= 'COVID 19')
    
    estado = models.BooleanField('Estado', default = True)
    

    class Meta:
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'
        ordering = ['aerolinea']

    def __str__(self):
        return self.aerolinea

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    idVuelo = models.IntegerField(blank= False, null= False)
    fechaHoraReserva = models.DateTimeField(default = timezone.now)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
       
    
    def __str__(self):
        return f'{self.user}: {self.idVuelo}'

