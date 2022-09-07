from typing import Dict

from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView

from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm

#Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):

    return render(request, "AppCoder/inicio.html")


def entregables(request):

    return render(request, "AppCoder/entregables.html")


# Formulario a mano
# def crear_curso(request):
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


def crear_curso(request):
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
    model = Estudiante
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('estudiantes')


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('estudiantes')


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')


# Views de ususarios, registro, login o logout

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        "form": formulario
    }
    if mensaje:
        context["mensaje"] = mensaje
    return render(request, "AppCoder/registro.html", context)


def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=contra)

                if user:
                    login(request=request, user=user)
                    return render(request,"AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                else:
                    return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"})
            else:
                return render(request,"AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()
      return render(request,"AppCoder/login.html", {'form':form} )


class CustomLogoutView(LogoutView):
    template_name = 'AppCoder/logout.html'

