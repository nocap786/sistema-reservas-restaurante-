from peewee import AutoField, CharField

from datos.modelos.models import ModelBase


class Cliente(ModelBase):
    id_cliente = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=20, null=True)
    correo = CharField(max_length=100, null=True)

    class Meta:
        table_name = "clientes"

    def mostrar_datos(self):
        print("=== CLIENTE ===")
        print(f"ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Telefono: {self.telefono or '-'}")
        print(f"Correo: {self.correo or '-'}")
