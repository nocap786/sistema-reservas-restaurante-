from auxiliares.opciones_menu import MENU_RESERVAS
from negocio import negocio_reservas
from presentacion.entradas import (
    confirmar,
    ejecutar_menu,
    mostrar_lista,
    mostrar_resultado,
    pedir_entero,
    pedir_fecha,
    pedir_hora,
)


def _registrar():
    id_cliente = pedir_entero("ID del cliente: ", minimo=1)
    id_mesa = pedir_entero("ID de la mesa: ", minimo=1)
    fecha = pedir_fecha()
    hora = pedir_hora()
    personas = pedir_entero("Cantidad de personas: ", minimo=1)
    mostrar_resultado(
        negocio_reservas.registrar_reserva(id_cliente, id_mesa, fecha, hora, personas)
    )


def _consultar():
    mostrar_lista("RESERVAS REGISTRADAS", negocio_reservas.listar_reservas(), "reservas")


def _buscar():
    fecha = pedir_fecha()
    mostrar_lista(
        "RESULTADOS", negocio_reservas.buscar_reservas_por_fecha(fecha), "reservas"
    )


def _modificar():
    id_reserva = pedir_entero("ID de la reserva: ", minimo=1)
    fecha = pedir_fecha("Nueva fecha (AAAA-MM-DD): ")
    hora = pedir_hora("Nueva hora (HH:MM): ")
    personas = pedir_entero("Nueva cantidad de personas: ", minimo=1)
    mostrar_resultado(
        negocio_reservas.modificar_reserva(id_reserva, fecha, hora, personas)
    )


def _cancelar():
    id_reserva = pedir_entero("ID de la reserva a cancelar: ", minimo=1)
    if confirmar("¿Confirmar cancelacion?"):
        mostrar_resultado(negocio_reservas.cancelar_reserva(id_reserva))


def menu_reservas():
    ejecutar_menu(
        "GESTION DE RESERVAS",
        MENU_RESERVAS,
        [_registrar, _consultar, _buscar, _modificar, _cancelar],
    )
