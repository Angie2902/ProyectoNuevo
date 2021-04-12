from django.contrib import admin
from .models import  Vuelos, Person, Reserva


admin.site.register(Person)
admin.site.register(Vuelos)
admin.site.register(Reserva)
