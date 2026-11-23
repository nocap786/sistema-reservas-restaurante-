from peewee import IntegrityError

from auxiliares.info_app import MSG_NO_ENCONTRADO
from auxiliares.validaciones import texto_valido
from datos.modelos.restaurante import Restaurante
from datos.repositorios import repo_restaurante


def _datos_validos(nombre, direccion, apertura, cierre):
    return (
        texto_valido(nombre, 100)
        and texto_valido(direccion, 150)
        and apertura < cierre
    )


def registrar_restaurante(nombre, direccion, apertura, cierre):
    if not _datos_validos(nombre, direccion, apertura, cierre):
        return False, "Datos invalidos. La hora de apertura debe ser menor a la de cierre."
    restaurante = Restaurante(
        nombre=nombre.strip(),
        direccion=direccion.strip(),
        horario_apertura=apertura,
        horario_cierre=cierre,
    )
    repo_restaurante.guardar(restaurante)
    return True, "Restaurante registrado correctamente."


def listar_restaurantes():
    return repo_restaurante.listar()


def buscar_restaurantes(texto):
    return repo_restaurante.buscar_por_nombre(texto.strip())


def modificar_restaurante(id_restaurante, nombre, direccion, apertura, cierre):
    restaurante = repo_restaurante.buscar_por_id(id_restaurante)
    if restaurante is None:
        return False, MSG_NO_ENCONTRADO.format("el restaurante")
    if not _datos_validos(nombre, direccion, apertura, cierre):
        return False, "Datos invalidos. La hora de apertura debe ser menor a la de cierre."
    restaurante.nombre = nombre.strip()
    restaurante.direccion = direccion.strip()
    restaurante.horario_apertura = apertura
    restaurante.horario_cierre = cierre
    repo_restaurante.guardar(restaurante)
    return True, "Restaurante modificado correctamente."


def eliminar_restaurante(id_restaurante):
    restaurante = repo_restaurante.buscar_por_id(id_restaurante)
    if restaurante is None:
        return False, MSG_NO_ENCONTRADO.format("el restaurante")
    try:
        repo_restaurante.eliminar(restaurante)
    except IntegrityError:
        return False, "No se puede eliminar: el restaurante tiene mesas asociadas."
    return True, "Restaurante eliminado correctamente."
