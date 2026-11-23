import bcrypt

from auxiliares.info_app import (
    MSG_LOGIN_FALLIDO,
    MSG_NO_ENCONTRADO,
    MSG_NOMBRE_USUARIO_INVALIDO,
    MSG_PASSWORD_INVALIDA,
)
from auxiliares.validaciones import nombre_usuario_valido, password_valida
from datos.modelos.usuario import Usuario
from datos.repositorios import repo_usuario


# ---------- Seguridad: hash BCrypt ----------

def hashear_password(password):
    """Devuelve el hash BCrypt (con salt) de la contraseña, como texto."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_password(password, password_hash):
    """Compara la contraseña ingresada con el hash guardado."""
    try:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
    except ValueError:
        return False


# ---------- Gestion de usuarios ----------

def no_hay_usuarios():
    return repo_usuario.contar() == 0


def registrar_usuario(nombre_usuario, password):
    nombre_usuario = nombre_usuario.strip()
    if not nombre_usuario_valido(nombre_usuario):
        return False, MSG_NOMBRE_USUARIO_INVALIDO
    if not password_valida(password):
        return False, MSG_PASSWORD_INVALIDA
    if repo_usuario.buscar_por_nombre(nombre_usuario) is not None:
        return False, "Ya existe un usuario con ese nombre."

    usuario = Usuario(
        nombre_usuario=nombre_usuario,
        password_hash=hashear_password(password),
        activo=True,
    )
    repo_usuario.guardar(usuario)
    return True, "Usuario registrado correctamente."


def listar_usuarios():
    return repo_usuario.listar()


def cambiar_password(id_usuario, nueva_password):
    usuario = repo_usuario.buscar_por_id(id_usuario)
    if usuario is None:
        return False, MSG_NO_ENCONTRADO.format("el usuario")
    if not password_valida(nueva_password):
        return False, MSG_PASSWORD_INVALIDA
    usuario.password_hash = hashear_password(nueva_password)
    repo_usuario.guardar(usuario)
    return True, "Contraseña actualizada correctamente."


def cambiar_estado(id_usuario, activo, id_usuario_actual):
    """Habilita o deshabilita un usuario (no se borra, queda deshabilitado)."""
    usuario = repo_usuario.buscar_por_id(id_usuario)
    if usuario is None:
        return False, MSG_NO_ENCONTRADO.format("el usuario")
    if not activo:
        if usuario.id_usuario == id_usuario_actual:
            return False, "No puede deshabilitar su propio usuario."
        if usuario.activo and repo_usuario.contar_activos() <= 1:
            return False, "Debe quedar al menos un usuario activo."
    usuario.activo = activo
    repo_usuario.guardar(usuario)
    return True, "Usuario habilitado." if activo else "Usuario deshabilitado."


# ---------- Login ----------

def autenticar(nombre_usuario, password):
    """Devuelve (ok, mensaje, usuario). El mensaje de error es siempre el mismo
    para no revelar si el usuario existe."""
    usuario = repo_usuario.buscar_por_nombre(nombre_usuario.strip())
    if usuario is None or not usuario.activo:
        return False, MSG_LOGIN_FALLIDO, None
    if not verificar_password(password, usuario.password_hash):
        return False, MSG_LOGIN_FALLIDO, None
    return True, "", usuario
