from peewee import AutoField, CharField, DateField, ForeignKeyField, IntegerField, TimeField

from datos.modelos.cliente import Cliente
from datos.modelos.mesa import Mesa
from datos.modelos.models import ModelBase


class Reserva(ModelBase):
    ESTADOS_VALIDOS = ("Pendiente", "Confirmada", "Cancelada", "Completada")
    ESTADOS_ACTIVOS = ("Pendiente", "Confirmada")

    id_reserva = AutoField()
    cliente = ForeignKeyField(Cliente, column_name="id_cliente", backref="reservas")
    mesa = ForeignKeyField(Mesa, column_name="id_mesa", backref="reservas")
    fecha = DateField()
    hora = TimeField()
    cantidad_personas = IntegerField()
    estado = CharField(max_length=20, default="Pendiente")

    class Meta:
        table_name = "reservas"

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError("Estado de reserva no valido")
        self.estado = nuevo_estado

    def mostrar_datos(self):
        print("=== RESERVA ===")
        print(f"ID Reserva: {self.id_reserva}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Mesa: {self.mesa.numero}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Personas: {self.cantidad_personas}")
        print(f"Estado: {self.estado}")
