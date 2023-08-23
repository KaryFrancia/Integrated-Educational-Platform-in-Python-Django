from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('crear_curso/', crear_curso),
    path('listar_cursos/', listar_cursos),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    path('entregables/', entregables, name="entregables"),
    path('pagos/', pagos, name="pagos"),
    path('busqueda/', busqueda, name="busqueda"),
    path('buscar_comision/', buscar_comision, name="buscar_comision"),
    path('buscar_pagos/', buscar_pagos, name="buscar_pagos"),
    path('buscar_estudiantes/', buscar_estudiantes, name="buscar_estudiantes"),
    path('buscar_profesores/', buscar_profesores, name="buscar_profesores"),
    path('buscar_entregables/', buscar_entregables, name="buscar_entregables"),
    path('eliminarProfesor/<id>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<id>', editarProfesor, name="editarProfesor"),
    path('estudiante/list/', EstudianteList.as_view(), name="estudiante_list"),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name="estudiante_crear"),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name="estudiante_borrar"),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name="estudiante_editar"),
    path('login/', Login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
