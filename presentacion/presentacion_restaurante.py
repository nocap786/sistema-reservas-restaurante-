from auxiliares.opciones_menu import MENU_CRUD
from negocio import negocio_restaurantes
from presentacion.entradas import (
    confirmar,
    ejecutar_menu,
    mostrar_lista,
    mostrar_resultado,
    pedir_entero,
    pedir_hora,
    pedir_texto,
)


def _registrar():
    nombre = pedir_texto("Nombre del restaurante: ")
    direccion = pedir_texto("Direccion: ")
    apertura = pedir_hora("Hora de apertura (HH:MM): ")
    cierre = pedir_hora("Hora de cierre (HH:MM): ")
    mostrar_resultado(
        negocio_restaurantes.registrar_restaurante(nombre, direccion, apertura, cierre)
    )


def _consultar():
    mostrar_lista("RESTAURANTES", negocio_restaurantes.listar_restaurantes(), "restaurantes")


def _buscar():
    texto = pedir_texto("Nombre a buscar: ")
    mostrar_lista("RESULTADOS", negocio_restaurantes.buscar_restaurantes(texto), "restaurantes")


def _modificar():
    id_restaurante = pedir_entero("ID del restaurante: ", minimo=1)
    nombre = pedir_texto("Nuevo nombre: ")
    direccion = pedir_texto("Nueva direccion: ")
    apertura = pedir_hora("Nueva hora de apertura (HH:MM): ")
    cierre = pedir_hora("Nueva hora de cierre (HH:MM): ")
    mostrar_resultado(
        negocio_restaurantes.modificar_restaurante(
            id_restaurante, nombre, direccion, apertura, cierre
        )
    )


def _eliminar():
    id_restaurante = pedir_entero("ID del restaurante: ", minimo=1)
    if confirmar("¿Confirmar eliminacion?"):
        mostrar_resultado(negocio_restaurantes.eliminar_restaurante(id_restaurante))


def menu_restaurantes():
    ejecutar_menu(
        "GESTION DE RESTAURANTES",
        MENU_CRUD,
        [_registrar, _consultar, _buscar, _modificar, _eliminar],
    )
