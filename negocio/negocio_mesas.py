from peewee import IntegrityError

from auxiliares.info_app import MSG_NO_ENCONTRADO
from auxiliares.validaciones import texto_valido
from datos.modelos.mesa import Mesa
from datos.repositorios import repo_mesa, repo_restaurante

MSG_DATOS_INVALIDOS = "Datos invalidos. El numero y la capacidad deben ser mayores a 0."


def _datos_validos(numero, capacidad, caracteristicas):
    if numero < 1 or capacidad < 1:
        return False
    return not caracteristicas or texto_valido(caracteristicas, 150)


def registrar_mesa(numero, capacidad, caracteristicas, id_restaurante):
    restaurante = repo_restaurante.buscar_por_id(id_restaurante)
    if restaurante is None:
        return False, MSG_NO_ENCONTRADO.format("el restaurante")
    if not _datos_validos(numero, capacidad, caracteristicas):
        return False, MSG_DATOS_INVALIDOS
    mesa = Mesa(
        numero=numero,
        capacidad=capacidad,
        caracteristicas=caracteristicas.strip() or None,
        restaurante=restaurante,
    )
    repo_mesa.guardar(mesa)
    return True, "Mesa registrada correctamente."


def listar_mesas():
    return repo_mesa.listar()


def buscar_mesas_por_capacidad(capacidad_minima):
    return repo_mesa.buscar_por_capacidad(capacidad_minima)


def modificar_mesa(id_mesa, numero, capacidad, caracteristicas):
    mesa = repo_mesa.buscar_por_id(id_mesa)
    if mesa is None:
        return False, MSG_NO_ENCONTRADO.format("la mesa")
    if not _datos_validos(numero, capacidad, caracteristicas):
        return False, MSG_DATOS_INVALIDOS
    mesa.numero = numero
    mesa.capacidad = capacidad
    mesa.caracteristicas = caracteristicas.strip() or None
    repo_mesa.guardar(mesa)
    return True, "Mesa modificada correctamente."


def eliminar_mesa(id_mesa):
    mesa = repo_mesa.buscar_por_id(id_mesa)
    if mesa is None:
        return False, MSG_NO_ENCONTRADO.format("la mesa")
    try:
        repo_mesa.eliminar(mesa)
    except IntegrityError:
        return False, "No se puede eliminar: la mesa tiene reservas asociadas."
    return True, "Mesa eliminada correctamente."
