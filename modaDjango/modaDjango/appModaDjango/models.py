from django.db import models
from .enum import plazo

class cliente(models.Model):
    documento=models.TextField(max_length=30, primary_key=True)
    nombre=models.TextField(max_length=30)
    apellido=models.TextField(max_length=30)
    edad=models.TextField(int)
    numero=models.TextField(int)

    def __str__(self):
        #txt="{0}{1}{2}{3}{4}"
        #return txt.format()
        return "{0}".format(self.documento)

class lineasCredito(models.Model):
    codigo=models.PositiveSmallIntegerField(primary_key=True, verbose_name="codigo")
    nombre=models.TextField(max_length=30)
    montoMax=models.PositiveBigIntegerField(verbose_name="Monto máximo")
    plazoMax=models.PositiveSmallIntegerField(verbose_name="Plazo máximo")
    def __str__(self):
        #txt="{0}{1}{2}{3}{4}"
        #return txt.format()
        return "{0}".format(self.codigo)

class credito(models.Model):
    documento=models.ForeignKey(cliente, null=True, on_delete=models.CASCADE) #es primaria en clientes
    codigo=models.ForeignKey(lineasCredito, null=False, on_delete=models.CASCADE)
    monto=models.PositiveBigIntegerField(verbose_name="Total crédito")
    plazo=models.PositiveSmallIntegerField(verbose_name="Plazo",choices=plazo,default=6)

    def __str__(self):
        #txt="{0}{1}{2}{3}{4}"
        #return txt.format()
        return "{0}".format(self.codigo)

class usuario(models.Model):
    documento=models.ForeignKey(cliente, null=True, on_delete=models.CASCADE) #es primaria en clientes
    usuario=models.TextField(max_length=30)
    clave=models.TextField(max_length=30)

    def __str__(self):
        #txt="{0}{1}{2}{3}{4}"
        #return txt.format()
        return "{0}".format(self.documento)

class empleado(models.Model):
    documento=models.ForeignKey(usuario, null=True, on_delete=models.CASCADE) #es primaria en clientes
    nombre=models.TextField(max_length=30)
    apellido=models.TextField(max_length=30) 
    correo=models.TextField(max_length=30) 
    celular=models.PositiveBigIntegerField(verbose_name="Teléfono celular")
    rol=models.TextField(max_length=30)
    def __str__(self):
        #txt="{0}{1}{2}{3}{4}"
        #return txt.format()
        return "{0}".format(self.documento)
