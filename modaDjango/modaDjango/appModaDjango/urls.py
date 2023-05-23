from django.urls import path
from .views import *

urlpatterns=[
    path('cliente',listadoCliente.as_view(), name='Clientes'),
    path('lineas',listadoLinea.as_view(), name='Lineas'),
    path('credito',listadoCredito.as_view(), name='Creditos'),
    path('usuario',listadoUsuario.as_view(), name='Usuarios'),
    path('empleado',listadoEmpleado.as_view(), name='Empleados')

]