from auxiliares.info_app import MSG_NO_ENCONTRADO
from datos.modelos.reserva import Reserva
from datos.repositorios import repo_cliente, repo_mesa, repo_reserva

MSG_CAPACIDAD = "La cantidad de personas debe ser mayor a 0 y no superar la capacidad de la mesa."
MSG_OCUPADA = "La mesa ya tiene una reserva activa en esa fecha y hora."


def registrar_reserva(id_cliente, id_mesa, fecha, hora, personas):
    cliente = repo_cliente.buscar_por_id(id_cliente)
    if cliente is None:
        return False, MSG_NO_ENCONTRADO.format("el cliente")
    mesa = repo_mesa.buscar_por_id(id_mesa)
    if mesa is None:
        return False, MSG_NO_ENCONTRADO.format("la mesa")
    if personas < 1 or personas > mesa.capacidad:
        return False, MSG_CAPACIDAD
    if repo_reserva.existe_reserva_activa(mesa, fecha, hora):
        return False, MSG_OCUPADA

    reserva = Reserva(
        cliente=cliente,
        mesa=mesa,
        fecha=fecha,
        hora=hora,
        cantidad_personas=personas,
        estado="Pendiente",
    )
    repo_reserva.guardar(reserva)
    return True, "Reserva registrada correctamente."


def listar_reservas():
    return repo_reserva.listar()


def buscar_reservas_por_fecha(fecha):
    return repo_reserva.buscar_por_fecha(fecha)


def modificar_reserva(id_reserva, fecha, hora, personas):
    reserva = repo_reserva.buscar_por_id(id_reserva)
    if reserva is None or reserva.estado == "Cancelada":
        return False, MSG_NO_ENCONTRADO.format("una reserva activa")
    if personas < 1 or personas > reserva.mesa.capacidad:
        return False, MSG_CAPACIDAD
    if repo_reserva.existe_reserva_activa(
        reserva.mesa, fecha, hora, excluir_id=reserva.id_reserva
    ):
        return False, MSG_OCUPADA

    reserva.fecha = fecha
    reserva.hora = hora
    reserva.cantidad_personas = personas
    repo_reserva.guardar(reserva)
    return True, "Reserva modificada correctamente."


def cancelar_reserva(id_reserva):
    reserva = repo_reserva.buscar_por_id(id_reserva)
    if reserva is None or reserva.estado == "Cancelada":
        return False, MSG_NO_ENCONTRADO.format("una reserva activa")
    reserva.cambiar_estado("Cancelada")
    repo_reserva.guardar(reserva)
    return True, "Reserva cancelada correctamente."
