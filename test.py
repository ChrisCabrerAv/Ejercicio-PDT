import unittest
from logica import Carrera, Postulante

class TestCarrera(unittest.TestCase):
    c1 = Carrera("INF",15,15,10,10,500,25,25)
    p1 = Postulante(500,500,500,500,700,700)

    def test_calculo(self):
        self.assertEqual(self.c1.calcular(self.p1),"600")