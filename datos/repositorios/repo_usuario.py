from datos.modelos.usuario import Usuario


def guardar(usuario):
    """Inserta o actualiza (Peewee decide segun si tiene clave primaria)."""
    usuario.save()
    return usuario


def listar():
    return list(Usuario.select().order_by(Usuario.id_usuario))


def buscar_por_id(id_usuario):
    return Usuario.get_or_none(Usuario.id_usuario == id_usuario)


def buscar_por_nombre(nombre_usuario):
    return Usuario.get_or_none(Usuario.nombre_usuario == nombre_usuario)


def contar():
    return Usuario.select().count()


def contar_activos():
    return Usuario.select().where(Usuario.activo == True).count()  # noqa: E712
