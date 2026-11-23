from datos.modelos.reserva import Reserva


def guardar(reserva):
    """Inserta o actualiza (Peewee decide segun si tiene clave primaria)."""
    reserva.save()
    return reserva


def listar():
    return list(Reserva.select().order_by(Reserva.fecha, Reserva.hora))


def buscar_por_id(id_reserva):
    return Reserva.get_or_none(Reserva.id_reserva == id_reserva)


def buscar_por_fecha(fecha):
    return list(
        Reserva.select()
        .where(Reserva.fecha == fecha)
        .order_by(Reserva.hora)
    )


def existe_reserva_activa(mesa, fecha, hora, excluir_id=None):
    """True si la mesa ya tiene una reserva activa en esa fecha y hora."""
    consulta = Reserva.select().where(
        (Reserva.mesa == mesa)
        & (Reserva.fecha == fecha)
        & (Reserva.hora == hora)
        & (Reserva.estado.in_(Reserva.ESTADOS_ACTIVOS))
    )
    if excluir_id is not None:
        consulta = consulta.where(Reserva.id_reserva != excluir_id)
    return consulta.exists()
