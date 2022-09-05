from typing import Dict

from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario


def inicio(request):

    return render(request, "AppCoder/inicio.html")


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


# Vistas de Cursos

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {'cursos': cursos})


def curso_formulario(request):
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'])
            curso.save()
            return render(request, "AppCoder/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = CursoFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_curso.html", {"formulario": formulario})


def busqueda_cursos(request):
    return render(request, "AppCoder/form_busqueda_curso.html")


def buscar_curso(request):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppCoder/cursos.html", {'cursos': cursos})
    else:
        return render(request, "AppCoder/cursos.html", {'cursos': []})


# Vistas de Profesores

def profesores(request):
    profesores = Profesor.objects.all()  # trae todos los profesores
    contexto = {"profesores": profesores}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppCoder/profesores.html", contexto)


def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    borrado_id = profesor.id
    profesor.delete()
    url_final = f"{reverse('profesores')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_profesor(request):
    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(**data)
            # profesor = Profesor(apellido=data['apellido'], nombre=data['nombre'])
            profesor.save()
            return redirect(reverse('profesores'))
    else:  # GET
        formulario = ProfesorFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_profesor.html", {"formulario": formulario})


def editar_profesor(request, id):
    # Recibe param profesor id, con el que obtenemos el profesor
    profesor = Profesor.objects.get(id=id)

    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.profesion = data['profesion']

            profesor.save()

            return redirect(reverse('profesores'))
    else:  # GET
        inicial = {
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
        }
        formulario = ProfesorFormulario(initial=inicial)
    return render(request, "AppCoder/form_profesor.html", {"formulario": formulario})


# Vistas de Estudiantes

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes.html'


class EstudianteCreateView(CreateView):
    pass


class EstudianteUpdateView(UpdateView):
    pass


class EstudianteDeleteView(DeleteView):
    pass
