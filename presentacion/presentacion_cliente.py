from auxiliares.opciones_menu import MENU_CRUD
from negocio import negocio_clientes
from presentacion.entradas import (
    confirmar,
    ejecutar_menu,
    mostrar_lista,
    mostrar_resultado,
    pedir_entero,
    pedir_texto,
)


def _registrar():
    nombre = pedir_texto("Nombre del cliente: ")
    telefono = pedir_texto("Telefono (opcional): ", obligatorio=False)
    correo = pedir_texto("Correo (opcional): ", obligatorio=False)
    mostrar_resultado(negocio_clientes.registrar_cliente(nombre, telefono, correo))


def _consultar():
    mostrar_lista("CLIENTES REGISTRADOS", negocio_clientes.listar_clientes(), "clientes")


def _buscar():
    texto = pedir_texto("Nombre a buscar: ")
    mostrar_lista("RESULTADOS", negocio_clientes.buscar_clientes(texto), "clientes")


def _modificar():
    id_cliente = pedir_entero("ID del cliente: ", minimo=1)
    nombre = pedir_texto("Nuevo nombre: ")
    telefono = pedir_texto("Nuevo telefono (opcional): ", obligatorio=False)
    correo = pedir_texto("Nuevo correo (opcional): ", obligatorio=False)
    mostrar_resultado(
        negocio_clientes.modificar_cliente(id_cliente, nombre, telefono, correo)
    )


def _eliminar():
    id_cliente = pedir_entero("ID del cliente: ", minimo=1)
    if confirmar("¿Confirmar eliminacion?"):
        mostrar_resultado(negocio_clientes.eliminar_cliente(id_cliente))


def menu_clientes():
    ejecutar_menu(
        "GESTION DE CLIENTES",
        MENU_CRUD,
        [_registrar, _consultar, _buscar, _modificar, _eliminar],
    )
