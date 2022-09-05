from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    # URLs de Cursos
    path('cursos/', views.cursos, name="cursos"),
    path('crear-curso/', views.curso_formulario, name="curso_formulario"),
    path('busqueda-curso-form/', views.busqueda_cursos, name="busqueda_curso_form"),
    path('busqueda-curso/', views.buscar_curso, name="busqueda_curso"),
    # URLs de Profesores
    path('profesores/', views.profesores, name="profesores"),
]
