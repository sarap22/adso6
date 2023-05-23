from django.views.generic import ListView
from appModaDjango.models import *
# Create your views here.
class listadoCliente(ListView):
    model=cliente
    template_name="index.html"

class listadoLinea(ListView):
    model=lineasCredito
    template_name="index1.html"

class listadoCredito(ListView):
    model=credito
    template_name="index2.html"

class listadoUsuario(ListView):
    model=usuario
    template_name="index3.html"
    
class listadoEmpleado(ListView):
    model=empleado
    template_name="index4.html"
    