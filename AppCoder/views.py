from typing import Dict

from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")


def cursos(request):

      return render(request, "AppCoder/cursos.html")


def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def curso_formulario(request):
      if request.method == 'POST':
            data_formulario: Dict = request.POST
            curso = Curso(nombre=data_formulario['nombre'], comision=data_formulario['comision'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
      else:  # GET
            return render(request, "AppCoder/form_curso.html")
