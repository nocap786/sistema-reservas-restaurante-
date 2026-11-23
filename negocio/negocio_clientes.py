from peewee import IntegrityError

from auxiliares.info_app import MSG_NO_ENCONTRADO
from auxiliares.validaciones import correo_valido, texto_valido
from datos.modelos.cliente import Cliente
from datos.repositorios import repo_cliente

MSG_DATOS_INVALIDOS = "Datos invalidos. Revise el nombre y el correo."


def _datos_validos(nombre, telefono, correo):
    if not texto_valido(nombre, 100):
        return False
    if telefono and len(telefono.strip()) > 20:
        return False
    if correo and not correo_valido(correo.strip()):
        return False
    return True


def registrar_cliente(nombre, telefono, correo):
    if not _datos_validos(nombre, telefono, correo):
        return False, MSG_DATOS_INVALIDOS
    cliente = Cliente(
        nombre=nombre.strip(),
        telefono=telefono.strip() or None,
        correo=correo.strip() or None,
    )
    repo_cliente.guardar(cliente)
    return True, "Cliente registrado correctamente."


def listar_clientes():
    return repo_cliente.listar()


def buscar_clientes(texto):
    return repo_cliente.buscar_por_nombre(texto.strip())


def modificar_cliente(id_cliente, nombre, telefono, correo):
    cliente = repo_cliente.buscar_por_id(id_cliente)
    if cliente is None:
        return False, MSG_NO_ENCONTRADO.format("el cliente")
    if not _datos_validos(nombre, telefono, correo):
        return False, MSG_DATOS_INVALIDOS
    cliente.nombre = nombre.strip()
    cliente.telefono = telefono.strip() or None
    cliente.correo = correo.strip() or None
    repo_cliente.guardar(cliente)
    return True, "Cliente modificado correctamente."


def eliminar_cliente(id_cliente):
    cliente = repo_cliente.buscar_por_id(id_cliente)
    if cliente is None:
        return False, MSG_NO_ENCONTRADO.format("el cliente")
    try:
        repo_cliente.eliminar(cliente)
    except IntegrityError:
        return False, "No se puede eliminar: el cliente tiene reservas asociadas."
    return True, "Cliente eliminado correctamente."
