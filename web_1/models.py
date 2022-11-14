from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField()

class Productos(models.Model):
    sku = models.IntegerField()
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField()
    stock = models.IntegerField()