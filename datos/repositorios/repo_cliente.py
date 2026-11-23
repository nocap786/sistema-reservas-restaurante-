from datos.modelos.cliente import Cliente


def guardar(cliente):
    """Inserta o actualiza (Peewee decide segun si tiene clave primaria)."""
    cliente.save()
    return cliente


def listar():
    return list(Cliente.select().order_by(Cliente.id_cliente))


def buscar_por_id(id_cliente):
    return Cliente.get_or_none(Cliente.id_cliente == id_cliente)


def buscar_por_nombre(texto):
    return list(
        Cliente.select()
        .where(Cliente.nombre.contains(texto))
        .order_by(Cliente.id_cliente)
    )


def eliminar(cliente):
    return cliente.delete_instance() > 0
