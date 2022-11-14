from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField()
    contraseña = models.CharField(max_length=50)

class Productos(models.Model):
    sku = models.IntegerField()
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=9)
    stock = models.IntegerField()

class Vendedores(models.Model):
    nombre_empresa = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    