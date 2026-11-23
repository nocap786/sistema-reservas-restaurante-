from peewee import AutoField, CharField, TimeField

from datos.modelos.models import ModelBase


class Restaurante(ModelBase):
    id_restaurante = AutoField()
    nombre = CharField(max_length=100)
    direccion = CharField(max_length=150)
    horario_apertura = TimeField()
    horario_cierre = TimeField()

    class Meta:
        table_name = "restaurantes"

    def esta_abierto(self, hora):
        return self.horario_apertura <= hora < self.horario_cierre

    def mostrar_datos(self):
        print("=== RESTAURANTE ===")
        print(f"ID: {self.id_restaurante}")
        print(f"Nombre: {self.nombre}")
        print(f"Direccion: {self.direccion}")
        print(f"Horario: {self.horario_apertura} - {self.horario_cierre}")
