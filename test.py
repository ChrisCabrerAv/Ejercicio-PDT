import unittest
from logica import Carrera

class TestCarrera(unittest.TestCase):
    c1 = Carrera("INF",15,15,10,10,500)
    
    def test_punteje_lenguaje(self):
        self.assertEqual(self.c1.get_puntaje_lenguaje(500),'75')

    def test_punteje_matematica(self):
        self.assertEqual(self.c1.get_puntaje_matematica(500),'75')

    def test_punteje_historia(self):
        self.assertEqual(self.c1.get_puntaje_historia(500),'50')

    def test_punteje_ciencias(self):
        self.assertEqual(self.c1.get_puntaje_ciencias(500),'50')

    def test_calculo(self):
        self.assertEqual(self.c1.calcular(700,700,500,500,500,500),"600")