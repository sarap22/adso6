from appModaDjango.models import *
from django.contrib import admin

@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display=('documento','nombre','apellido','edad','numero')
    #ordering=("-nombre",)
    #list_display_links=('nombre','apellido')
    #list_editable=('documento','nombre','apellido','edad','numero')
    list_filter=("nombre",)
    list_per_page= 20

@admin.register(credito)
class creditoAdmin(admin.ModelAdmin):
    list_display=('documento','codigo','monto','plazo')
    search_fields=('documento','codigo','monto','plazo')

@admin.register(lineasCredito)
class lineasCreditoAdmin(admin.ModelAdmin):
    list_display=('codigo','nombre','montoMax','plazoMax')
    search_fields=('codigo','nombre','montoMax','plazoMax')

@admin.register(usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display=('documento','usuario','clave')
    search_fields=('documento','usuario','clave')

@admin.register(empleado)
class empleadoAdmin(admin.ModelAdmin):
    list_display=('documento','nombre','apellido','correo','celular','rol')
    search_fields=('documento','nombre','apellido','correo','celular','rol')



