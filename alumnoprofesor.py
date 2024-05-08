import unittest

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = []

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__


class Alumno:
    def __init__(self, nombre, legajo):
        self.__nombre__ = nombre
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_legajo(self):
        return self.__legajo__


class TestMateria(unittest.TestCase):
    def test_constructor(self):
        profesores = ["Profesor1", "Profesor2"]
        materia = Materia("Matemáticas", profesores)
        self.assertEqual(materia._materia__nombre__, "Matemáticas")
        self.assertEqual(materia._materia__profesores__, profesores)
        self.assertEqual(materia._materia__alumnos__,)

    def test_obtener_profesores(self):
        profesores = ["Profesor1", "Profesor2"]
        materia = Materia("Matemáticas", profesores)
        self.assertEqual(materia.obtener_profesores(), profesores)

    def test_cambiar_nombre(self):
        materia = Materia("Matemáticas", [])
        materia.cambiar_nombre("Física")
        self.assertEqual(materia._Materia__nombre__, "Física")

    def test_obtener_alumnos(self):
        materia = Materia("Matemáticas", [])
        self.assertEqual(materia.obtener_alumnos(), [])


class TestProfesor(unittest.TestCase):
    def test_constructor(self):
        profesor = Profesor("Juan", "Docente", 123)
        self.assertEqual(profesor._profesor__nombre__, "Juan")
        self.assertEqual(profesor._profesor__cargo__, "Docente")
        self.assertEqual(profesor._profesor__legajo__, 123)

    def test_obtener_nombre(self):
        profesor = Profesor("Juan", "Docente", 123)
        self.assertEqual(profesor.obtener_nombre(), "Juan")

    def test_obtener_cargo(self):
        profesor = Profesor("Juan", "Docente", 123)
        self.assertEqual(profesor.obtener_cargo(), "Docente")

    def test_obtener_legajo(self):
        profesor = Profesor("Juan", "Docente", 123)
        self.assertEqual(profesor.obtener_legajo(), 123)


if __name__ == '__main__':
    unittest.main()