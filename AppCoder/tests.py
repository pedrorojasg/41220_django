import random
import string

from django.test import TestCase
from AppCoder.models import Profesor

class ProfesorTestCase(TestCase):

    def test_creacion_profesores(self):
        # Test 1: Comprobar puedo crear un profesor con un nombre con letras random
        lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        nombre_prueba = "".join(lista_letras_nombre)
        apellido_prueba = "".join(lista_letras_apellido)
        profesor_1 = Profesor.objects.create(nombre=nombre_prueba, apellido=apellido_prueba)

        self.assertIsNotNone(profesor_1.id)
        self.assertEqual(profesor_1.nombre, nombre_prueba)
        self.assertEqual(profesor_1.apellido, apellido_prueba)
