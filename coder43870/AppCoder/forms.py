from django import forms

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

