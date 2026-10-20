from datos.modelos.cliente import Persona


class Mesa:
    def __init__(self, id_mesa, numero, capacidad, caracteristicas):
        self._id_mesa = id_mesa
        self._numero = numero
        self._capacidad = capacidad
        self._caracteristicas = caracteristicas

    @property
    def numero(self):
        return self._numero

    @property
    def capacidad(self):
        return self._capacidad

    def mostrar_datos(self):
        print(f"Mesa: {self._numero}")
        print(f"Capacidad: {self._capacidad}")
        print(f"Caracteristicas: {self._caracteristicas}")


def mostrar_informacion(objeto):
    objeto.mostrar_datos()