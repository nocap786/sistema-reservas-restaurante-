from auxiliares.opciones_menu import MENU_CRUD
from negocio import negocio_mesas
from presentacion.entradas import (
    confirmar,
    ejecutar_menu,
    mostrar_lista,
    mostrar_resultado,
    pedir_entero,
    pedir_texto,
)


def _registrar():
    numero = pedir_entero("Numero de mesa: ", minimo=1)
    capacidad = pedir_entero("Capacidad: ", minimo=1)
    caracteristicas = pedir_texto("Caracteristicas (opcional): ", obligatorio=False)
    id_restaurante = pedir_entero("ID del restaurante: ", minimo=1)
    mostrar_resultado(
        negocio_mesas.registrar_mesa(numero, capacidad, caracteristicas, id_restaurante)
    )


def _consultar():
    mostrar_lista("MESAS REGISTRADAS", negocio_mesas.listar_mesas(), "mesas")


def _buscar():
    capacidad = pedir_entero("Capacidad minima: ", minimo=1)
    mostrar_lista(
        "RESULTADOS", negocio_mesas.buscar_mesas_por_capacidad(capacidad), "mesas"
    )


def _modificar():
    id_mesa = pedir_entero("ID de la mesa: ", minimo=1)
    numero = pedir_entero("Nuevo numero: ", minimo=1)
    capacidad = pedir_entero("Nueva capacidad: ", minimo=1)
    caracteristicas = pedir_texto("Nuevas caracteristicas (opcional): ", obligatorio=False)
    mostrar_resultado(
        negocio_mesas.modificar_mesa(id_mesa, numero, capacidad, caracteristicas)
    )


def _eliminar():
    id_mesa = pedir_entero("ID de la mesa: ", minimo=1)
    if confirmar("¿Confirmar eliminacion?"):
        mostrar_resultado(negocio_mesas.eliminar_mesa(id_mesa))


def menu_mesas():
    ejecutar_menu(
        "GESTION DE MESAS",
        MENU_CRUD,
        [_registrar, _consultar, _buscar, _modificar, _eliminar],
    )
