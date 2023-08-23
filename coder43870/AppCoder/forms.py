from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)

class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class EntregableForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    fecha_entrega=forms.DateField()
    entregado=forms.BooleanField()

class PagoForm(forms.Form):
    cliente = forms.CharField(max_length=50)
    monto = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = forms.DateField()

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
       model=User
       fields=["username", "email", "password1", "password2"]
       help_texts = {campo:"" for campo in fields}

