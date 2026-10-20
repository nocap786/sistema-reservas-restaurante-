class Mesa:
    def __init__(self, id_mesa, numero, capacidad, caracteristicas):
        self.id_mesa = id_mesa
        self.numero = numero
        self.capacidad = capacidad
        self.caracteristicas = caracteristicas

    def mostrar_datos(self):
        print(f"ID: {self.id_mesa}")
        print(f"Numero: {self.numero}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Caracteristicas: {self.caracteristicas}")