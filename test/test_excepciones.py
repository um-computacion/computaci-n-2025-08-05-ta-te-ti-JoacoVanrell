import unittest
from src.excepciones import PosOcupadaException, Ganador, Empate

class TestExcepciones(unittest.TestCase):
    def test_posicion_ocupada_exception(self):
        with self.assertRaises(PosOcupadaException):
            raise PosOcupadaException()

    def test_ganador_exception(self):
        with self.assertRaises(Ganador):
            raise Ganador()

    def test_empate_exception(self):
        with self.assertRaises(Empate):
            raise Empate()

    def test_son_subclases_de_exception(self):
        for cls in (PosOcupadaException, Ganador, Empate):
            self.assertTrue(issubclass(cls, Exception))

if __name__ == "__main__":
    unittest.main()
