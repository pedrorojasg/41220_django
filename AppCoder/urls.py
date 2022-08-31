from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio), #esta era nuestra primer view
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('crear-curso/', views.curso_formulario, name="curso_formulario"),
]
