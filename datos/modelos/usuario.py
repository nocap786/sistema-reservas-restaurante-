from peewee import AutoField, BooleanField, CharField

from datos.modelos.models import ModelBase


class Usuario(ModelBase):
    id_usuario = AutoField()
    nombre_usuario = CharField(max_length=50, unique=True)
    password_hash = CharField(max_length=255)
    activo = BooleanField(default=True)

    class Meta:
        table_name = "usuarios"

    def mostrar_datos(self):
        # Nunca se muestra la contraseña ni su hash.
        print("=== USUARIO ===")
        print(f"ID: {self.id_usuario}")
        print(f"Usuario: {self.nombre_usuario}")
        print(f"Estado: {'Activo' if self.activo else 'Deshabilitado'}")
