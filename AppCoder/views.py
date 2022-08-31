from typing import Dict

from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario


def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")


def cursos(request):
      cursos = Curso.objects.all()
      return render(request, "AppCoder/cursos.html", {'cursos': cursos})


def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


# Formulario a mano
# def curso_formulario(request):
#       if request.method == 'POST':
#             data_formulario: Dict = request.POST
#             curso = Curso(nombre=data_formulario['nombre'], comision=data_formulario['comision'])
#             curso.save()
#             return render(request, "AppCoder/inicio.html")
#       else:  # GET
#             return render(request, "AppCoder/form_curso.html")


def curso_formulario(request):
      if request.method == 'POST':
            formulario= CursoFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  curso = Curso(nombre=data['nombre'], comision=data['comision'])
                  curso.save()
                  return render(request, "AppCoder/inicio.html", {"exitoso": True})
      else:  # GET
            formulario= CursoFormulario()  # Formulario vacio para construir el html
      return render(request, "AppCoder/form_curso.html", {"formulario": formulario})


def busqueda_cursos(request):
      return render(request, "AppCoder/form_busqueda_curso.html")


def buscar(request):
      if request.GET["comision"]:
            comision = request.GET["comision"]
            cursos = Curso.objects.filter(comision__icontains=comision)
            return render(request, "AppCoder/cursos.html", {'cursos': cursos})
      else:
            return render(request, "AppCoder/cursos.html", {'cursos': []})
