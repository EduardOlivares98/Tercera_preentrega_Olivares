from django.db import models

# Create your models here.

class piezaCarro(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()

class tipoCarro(models.Model):
    nombre = models.CharField (max_length=50)
    marca = models.CharField(max_length=50)
    numero = models.IntegerField()

class profesionales(models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    especialidad = models.CharField(max_length=50)