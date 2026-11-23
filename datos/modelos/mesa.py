from peewee import AutoField, CharField, ForeignKeyField, IntegerField

from datos.modelos.models import ModelBase
from datos.modelos.restaurante import Restaurante


class Mesa(ModelBase):
    id_mesa = AutoField()
    numero = IntegerField()
    capacidad = IntegerField()
    caracteristicas = CharField(max_length=150, null=True)
    restaurante = ForeignKeyField(
        Restaurante, column_name="id_restaurante", backref="mesas"
    )

    class Meta:
        table_name = "mesas"

    def mostrar_datos(self):
        print("=== MESA ===")
        print(f"ID: {self.id_mesa}")
        print(f"Numero: {self.numero}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Caracteristicas: {self.caracteristicas or '-'}")
        print(f"Restaurante: {self.restaurante.nombre}")
