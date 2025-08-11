import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_creacion_jugador(self):
        j = Jugador("Agus", "X", "Jugando")
        self.assertEqual(j.nombre, "Agus")
        self.assertEqual(j.ficha, "X")
        self.assertEqual(j.estado, "Jugando")

    def test_con_ficha_cero(self):
        j = Jugador("Joaquin", "0", "Jugando")
        self.assertEqual(j.ficha, "0")

    def test_atributos_modificables(self):
        j = Jugador("Francisco", "X", "Jugando")
        j.nombre = "Nuevo Francisco"
        j.ficha = "0"
        j.estado = "Ganador"
        self.assertEqual(j.nombre, "Nuevo Francisco")
        self.assertEqual(j.ficha, "0")
        self.assertEqual(j.estado, "Ganador")

    def test_objetos_distintos(self):
        j1 = Jugador("Antonio", "X", "Jugando")
        j2 = Jugador("Evangelina", "X", "Jugando")
        self.assertIsNot(j1, j2)

if __name__ == "__main__":
    unittest.main()

