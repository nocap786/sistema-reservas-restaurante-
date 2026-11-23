from datos.modelos.mesa import Mesa


def guardar(mesa):
    """Inserta o actualiza (Peewee decide segun si tiene clave primaria)."""
    mesa.save()
    return mesa


def listar():
    return list(Mesa.select().order_by(Mesa.id_mesa))


def buscar_por_id(id_mesa):
    return Mesa.get_or_none(Mesa.id_mesa == id_mesa)


def buscar_por_capacidad(capacidad_minima):
    return list(
        Mesa.select()
        .where(Mesa.capacidad >= capacidad_minima)
        .order_by(Mesa.capacidad, Mesa.id_mesa)
    )


def eliminar(mesa):
    return mesa.delete_instance() > 0
