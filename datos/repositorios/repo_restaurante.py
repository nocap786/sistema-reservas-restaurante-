from datos.modelos.restaurante import Restaurante


def guardar(restaurante):
    """Inserta o actualiza (Peewee decide segun si tiene clave primaria)."""
    restaurante.save()
    return restaurante


def listar():
    return list(Restaurante.select().order_by(Restaurante.id_restaurante))


def buscar_por_id(id_restaurante):
    return Restaurante.get_or_none(Restaurante.id_restaurante == id_restaurante)


def buscar_por_nombre(texto):
    return list(
        Restaurante.select()
        .where(Restaurante.nombre.contains(texto))
        .order_by(Restaurante.id_restaurante)
    )


def eliminar(restaurante):
    return restaurante.delete_instance() > 0
