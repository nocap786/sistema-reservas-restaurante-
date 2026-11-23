"""Utilidades de entrada y salida por consola (solo interaccion con el usuario)."""

import maskpass

from auxiliares.info_app import (
    MSG_CAMPO_OBLIGATORIO,
    MSG_ENTERO_INVALIDO,
    MSG_FECHA_INVALIDA,
    MSG_HORA_INVALIDA,
    MSG_OPCION_INVALIDA,
    MSG_SIN_REGISTROS,
)
from auxiliares.validaciones import parsear_fecha, parsear_hora

ANCHO = 40


def mostrar_menu(titulo, opciones):
    print("\n" + "=" * ANCHO)
    print(titulo.center(ANCHO))
    print("=" * ANCHO)
    for numero, texto in enumerate(opciones, start=1):
        print(f"{numero}. {texto}")
    print("=" * ANCHO)
    return input("Seleccione una opcion: ").strip()


def ejecutar_menu(titulo, opciones, acciones):
    """Muestra el menu en bucle. La ultima opcion siempre es 'volver'."""
    while True:
        opcion = mostrar_menu(titulo, opciones)
        if opcion == str(len(opciones)):
            return
        if opcion.isdigit() and 1 <= int(opcion) <= len(acciones):
            acciones[int(opcion) - 1]()
        else:
            print(MSG_OPCION_INVALIDA)


def pedir_texto(mensaje, obligatorio=True):
    while True:
        valor = input(mensaje).strip()
        if valor or not obligatorio:
            return valor
        print(MSG_CAMPO_OBLIGATORIO)


def pedir_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print(MSG_ENTERO_INVALIDO)
            continue
        if minimo is not None and valor < minimo:
            print(f"El valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def pedir_fecha(mensaje="Fecha (AAAA-MM-DD): "):
    while True:
        fecha = parsear_fecha(input(mensaje))
        if fecha is not None:
            return fecha
        print(MSG_FECHA_INVALIDA)


def pedir_hora(mensaje="Hora (HH:MM): "):
    while True:
        hora = parsear_hora(input(mensaje))
        if hora is not None:
            return hora
        print(MSG_HORA_INVALIDA)


def pedir_password(mensaje="Contraseña: "):
    """Pide la contraseña ocultandola con Maskpass (se muestra como *)."""
    return maskpass.askpass(prompt=mensaje, mask="*")


def confirmar(mensaje):
    return input(f"{mensaje} (s/n): ").strip().lower() == "s"


def pausar():
    input("\nPresione Enter para continuar...")


def mostrar_resultado(resultado):
    """Imprime el mensaje de un resultado (ok, mensaje)."""
    print(resultado[1])


def mostrar_lista(titulo, entidades, nombre_plural):
    """Polimorfismo: cada entidad (Cliente, Mesa, Reserva...) responde a
    mostrar_datos() a su manera, sin que esta funcion sepa de que clase es."""
    print(f"\n========== {titulo} ==========")
    if not entidades:
        print(MSG_SIN_REGISTROS.format(nombre_plural))
    for entidad in entidades:
        entidad.mostrar_datos()
        print("-" * ANCHO)
    pausar()
