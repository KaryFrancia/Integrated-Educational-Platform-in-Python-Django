from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}, profesion: {self.profesion} "

class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"{self.nombre} - {self.entregado}"

class Pago(models.Model):
    cliente = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    def __str__(self):
        return f"Pago de {self.cliente} - {self.fecha_pago}, monto: {self.monto}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
