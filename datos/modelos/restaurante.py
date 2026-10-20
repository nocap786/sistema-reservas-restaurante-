class Restaurante:
    def __init__(self, id_restaurante, nombre, direccion, horario_apertura, horario_cierre):
        self.id_restaurante = id_restaurante
        self.nombre = nombre
        self.direccion = direccion
        self.horario_apertura = horario_apertura
        self.horario_cierre = horario_cierre

    def mostrar_datos(self):
        print(f"ID: {self.id_restaurante}")
        print(f"Nombre: {self.nombre}")
        print(f"Direccion: {self.direccion}")
        print(f"Horario: {self.horario_apertura} - {self.horario_cierre}")