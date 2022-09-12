import random
import string

from django.test import TestCase
from AppCoder.models import Profesor

class ProfesorTestCase(TestCase):
    def setUp(self):
        # Aqui va data inicial que podrías usar en los otros tests
        # Por ejemplo:
        # self.profesor_1 = Profesor.objects.create(name="Nombre 1", apellido="Apellido 1")
        pass

    def test_creacion_profesores(self):
        """Profesoress"""
        # Test 1: creación nombre o apellido con letras aleatorias
        lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        nombre_prueba = "".join(lista_letras_nombre)
        apellido_prueba = "".join(lista_letras_apellido)
        profesor_1 = Profesor.objects.create(nombre=nombre_prueba, apellido=apellido_prueba)

        self.assertIsNotNone(profesor_1.id)
        self.assertEqual(profesor_1.nombre, nombre_prueba)
        self.assertEqual(profesor_1.apellido, apellido_prueba)

        # Test 2: creación nombre o apellido vacio
        profesor_1 = Profesor.objects.create(nombre='', apellido='')
        # ?
