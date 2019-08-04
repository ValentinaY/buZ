from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    placas = models.CharField(primary_key=True, max_length=50)
    tecnomecanica = models.CharField(max_length=50)

class Acuerdo(models.Model):
    placas = models.CharField(primary_key=True, max_length=50)
    direccionInicial = models.CharField(max_length=50)
    direccionFinal = models.CharField(max_length=50)
    hora = models.CharField(max_length=50, default=" ")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)


class Trabajador(models.Model):
    cedula = models.CharField(primary_key=True, max_length=30, unique= True)
    nombre = models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    correo_electronico= models.CharField(max_length=60, unique= True)
    contrasena = models.CharField(max_length=128)
    acuerdoAsociado = models.ForeignKey(Acuerdo, on_delete=models.CASCADE, default=" ")

class Conductor(models.Model):
    cedula = models.CharField(primary_key=True, max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=60, unique=True)
    contrasena = models.CharField(max_length=128)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, default=" ")

