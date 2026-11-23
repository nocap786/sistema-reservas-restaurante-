from peewee import Model

from datos.conexion import db


class ModelBase(Model):
    """Modelo base de Peewee.

    Centraliza la conexion a la BD (todos los modelos heredan de aqui) y define
    el metodo mostrar_datos(), que cada modelo sobrescribe (polimorfismo).
    """

    class Meta:
        database = db

    def mostrar_datos(self):
        raise NotImplementedError("Cada modelo debe implementar mostrar_datos()")
