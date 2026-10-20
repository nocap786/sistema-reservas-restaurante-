class Restaurante:
    def __init__(self, id_restaurante, nombre, direccion, horario_apertura, horario_cierre):
        self._id_restaurante = id_restaurante
        self._nombre = nombre
        self._direccion = direccion
        self._horario_apertura = horario_apertura
        self._horario_cierre = horario_cierre

    @property
    def nombre(self):
        return self._nombre

    def esta_abierto(self, hora):
        return self._horario_apertura <= hora < self._horario_cierre

    def mostrar_datos(self):
        print(f"ID: {self._id_restaurante}")
        print(f"Nombre: {self._nombre}")
        print(f"Direccion: {self._direccion}")
        print(f"Horario: {self._horario_apertura} - {self._horario_cierre}")