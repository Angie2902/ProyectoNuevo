from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name ='index'),
    path('profile/', views.profile, name ='profile'),
    path('register/', views.register, name ='register'),
    path('login/', LoginView.as_view(template_name ='Tuluayork/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name ='Tuluayork/logout.html'), name = 'logout'),
    
    
    path('Vuelos/', views.mostrarVuelos, name ='mostarVuelos'),
    path('mostrarVuelosAbril/', views.mostrarVuelosAbril, name ='mostrarVuelosAbril'),
    path('crearVuelo/', views.crearVuelo, name ='crearVuelo'),
    path('detalleVuelos/<int:id>', views.detalleVuelos, name ='detalleVuelos'),
    path('editar_vuelo/<int:id>', views.editarVuelo, name ='editar_vuelo'),
    path('eliminarVuelo/<int:id>', views.EliminarVuelo, name ='eliminarVuelo'),

    path('Usuario/', views.mostrarUsuario, name ='mostarusuario'),
    path('editar_usuario/<int:id>', views.editarUsuario, name ='editar_usuario'),
    path('eliminarusuario/<int:id>', views.EliminarUsuario, name ='eliminarusuario'),

    path('crearReserva/<int:id>', views.crearReserva, name ='crearReserva'),
    path('mostrar_reserva/', views.mostrarReservas, name ='mostrarReservas'),
    path('eliminar_reserva/<int:id>', views.EliminarReserva, name ='eliminarReservas'),




    path('weather/', views.indexApi, name='weather'),

   
    

    
] 