from django.db import models


"""
Estudiantes (nombre, apellido, email)
Profesor (nombre, apellido, email, profesión)
Entregable (nombre, fechaDeEntrega,entregado)
Curso (nombre, comisión)
"""

class Estudiante(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    profesion = models.CharField(max_length=64)


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    comision = models.IntegerField()


class Entregable(models.Model):
    nombre = models.CharField(max_length=128)
    entregado = models.BooleanField()
    fecha_de_entrega = models.DateField()
