
from datos.repositorio.reserva_repositorio import (
    registrar_reserva,
    consultar_reservas,
    modificar_reserva,
    cancelar_reserva
)


class GestionReservas:

    def registrar(self, id_cliente, id_mesa, fecha, hora, personas):
        if personas <= 0:
            return False

        return registrar_reserva(
            id_cliente, id_mesa, fecha, hora, personas
        )

    def consultar(self):
        return consultar_reservas()

    def modificar(self, id_reserva, fecha, hora, personas):
        if personas <= 0:
            return False

        return modificar_reserva(
            id_reserva, fecha, hora, personas
        )

    def cancelar(self, id_reserva):
        return cancelar_reserva(id_reserva)
