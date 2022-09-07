from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('entregables/', views.entregables, name="entregables"),
    # URLs de Cursos
    path('cursos/', views.cursos, name="cursos"),
    path('crear-curso/', views.crear_curso, name="crear_curso"),
    path('busqueda-curso-form/', views.busqueda_cursos, name="busqueda_curso_form"),
    path('busqueda-curso/', views.buscar_curso, name="busqueda_curso"),
    # URLs de Profesores
    path('profesores/', views.profesores, name="profesores"),
    path('crear-profesor/', views.crear_profesor, name="crear_profesor"),
    path('editar-profesor/<int:id>/', views.editar_profesor, name="editar_profesor"),
    path('eliminar-profesor/<int:id>/', views.eliminar_profesor, name="eliminar_profesor"),
    # URLs de Estudiantes
    path('estudiantes/', views.EstudianteListView.as_view(), name="estudiantes"),
    path('crear-estudiante/', views.EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', views.EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', views.EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
]
