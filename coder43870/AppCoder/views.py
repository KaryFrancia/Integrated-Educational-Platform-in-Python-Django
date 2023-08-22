from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def crear_curso(request):
    nombre_curso="Programacion basica"
    comision_curso=99998
    print("creando curso")
    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"curso creado: {curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos=Curso.objects.all()
    respuesta=''
    for curso in cursos:
        respuesta+=f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def profesores(request):
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profesor=Profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            mensaje="Profesor creado"           
        else:
            mensaje="Datos invalidos"
        formulario_profesor=ProfesorForm()
        return render(request,"AppCoder/profesores.html", {"mensaje":mensaje,"formulario": formulario_profesor})
    else:
        formulario_profesor=ProfesorForm()
        profesores=Profesor.objects.all()
    return render(request,"AppCoder/profesores.html", {"formulario": formulario_profesor, "profesores": profesores})


def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            mensaje="Curso creado"           
        else:
            mensaje="Datos invalidos"
        formulario_curso=CursoForm()
        return render(request, "AppCoder/cursos.html", {"mensaje":mensaje, "formulario": formulario_curso})
    else:
        formulario_curso=CursoForm()
        cursos=Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {"formulario": formulario_curso, "cursos": cursos})


#def estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            estudiante=Estudiante(nombre=nombre,apellido=apellido,email=email)
            estudiante.save()
            mensaje="Estudiante registrado"           
        else:
            mensaje="Datos invalidos"
        formulario_estudiante=EstudianteForm()
        return render(request, "AppCoder/estudiantes.html", {"mensaje":mensaje, "formulario": formulario_estudiante})
    else:
        formulario_estudiante=EstudianteForm()
        estudiantes=Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"formulario": formulario_estudiante, "estudiantes":estudiantes})
            
def entregables(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            fecha_entrega=info["fecha_entrega"]
            entregado=info["entregado"]
            entregable=Entregable(nombre=nombre,fecha_entrega=fecha_entrega,entregado=entregado)
            entregable.save()
            mensaje="Entregable realizado"           
        else:
            mensaje="Datos invalidos"
        formulario_entregable=EntregableForm()
        return render(request, "AppCoder/entregables.html", {"mensaje":mensaje, "formulario": formulario_entregable})
    else:
        formulario_entregable=EntregableForm()
        entregables=Entregable.objects.all()
    return render(request, "AppCoder/entregables.html", {"formulario": formulario_entregable, "entregables":entregables})
    
def pagos(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cliente=info["cliente"]
            monto=info["monto"]
            fecha_pago=info["fecha_pago"]
            pago=Pago(cliente=cliente,monto=monto,fecha_pago=fecha_pago)
            pago.save()
            mensaje="Pago realizado"           
        else:
            mensaje="Datos invalidos"
        formulario_pago=PagoForm()
        return render(request, "AppCoder/pagos.html", {"mensaje":mensaje, "formulario": formulario_pago})
    else:
        formulario_pago=PagoForm()
        pagos=Pago.objects.all()
    return render(request, "AppCoder/pagos.html", {"formulario": formulario_pago, "pagos":pagos})

def busqueda(request):
    return render(request, "AppCoder/busqueda.html" )

def buscar_comision (request):
    comision=request.GET["comision"]
    if comision!="":
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"AppCoder/busqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/busqueda.html", {"mensaje": "No ingresaste información"})
    
def buscar_pagos(request):
    cliente = request.GET["cliente"]
    if cliente!="":
        pagos = Pago.objects.filter(cliente__icontains=cliente)     
        return render(request, 'AppCoder/busqueda.html', {'pagos': pagos})
    else:
       return render(request, 'AppCoder/busqueda.html', {"mensaje": "No ingresaste información"})

def buscar_estudiantes(request):
    email = request.GET["email"]
    if email!="":
        estudiantes = Estudiante.objects.filter(email__icontains=email)     
        return render(request, 'AppCoder/busqueda.html', {'estudiantes': estudiantes})
    else:
       return render(request, 'AppCoder/busqueda.html', {"mensaje": "No ingresaste información"})

def buscar_profesores(request):
    profesion = request.GET["profesion"]
    if profesion!="":
        profesores = Profesor.objects.filter(profesion__icontains=profesion)     
        return render(request, 'AppCoder/busqueda.html', {'profesores': profesores})
    else:
       return render(request, 'AppCoder/busqueda.html', {"mensaje": "No ingresaste información"})

def buscar_entregables(request):
    nombre = request.GET["nombre"]
    if nombre!="":
        entregables = Entregable.objects.filter(nombre__icontains=nombre)     
        return render(request, 'AppCoder/busqueda.html', {'entregables': entregables})
    else:
       return render(request, 'AppCoder/busqueda.html', {"mensaje": "No ingresaste información"})

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    profesores=Profesor.objects.all()
    formulario_profesor=ProfesorForm()
    mensaje="Profesor eliminado"
    return render(request,"AppCoder/profesores.html", {"mensaje":mensaje, "formulario":formulario_profesor, "profesores":profesores})

def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.save()
            mensaje="Profesor editado"
            profesores=Profesor.objects.all()
            formulario_profesor=ProfesorForm()
            return render(request,"AppCoder/profesores.html", {"mensaje":mensaje, "formulario": formulario_profesor, "profesores": profesores})
    else:
        
        formulario_profesor=ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
    return render(request,"AppCoder/editarProfesor.html", {"formulario":formulario_profesor, "profesor":profesor})


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

class EstudianteList(ListView):
    model= Estudiante
    template_name= "AppCoder/estudiantes.html"

class EstudianteCreacion(CreateView):
    model= Estudiante
    success_url= reverse_lazy("estudiante_list")
    fields=['nombre', 'apellido', 'email']


class EstudianteDetalle(DetailView):
    model=Estudiante
    template_name="AppCoder/estudiante_detalle.html"


class EstudianteDelete(DeleteView):
    model=Estudiante
    success_url= reverse_lazy("estudiante_list")


class EstudianteUpdate(UpdateView):
    model= Estudiante
    success_url= reverse_lazy("estudiante_list")
    fields=['nombre', 'apellido', 'email']
