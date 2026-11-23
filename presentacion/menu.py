from auxiliares.info_app import APP_NOMBRE
from auxiliares.opciones_menu import MENU_PRINCIPAL
from presentacion.entradas import ejecutar_menu
from presentacion.presentacion_cliente import menu_clientes
from presentacion.presentacion_mesa import menu_mesas
from presentacion.presentacion_reserva import menu_reservas
from presentacion.presentacion_restaurante import menu_restaurantes
from presentacion.presentacion_usuario import menu_usuarios


def menu_principal(usuario):
    """Menu principal. Solo se llega aqui despues de iniciar sesion."""
    print(f"\n{APP_NOMBRE}")
    ejecutar_menu(
        f"MENU PRINCIPAL ({usuario.nombre_usuario})",
        MENU_PRINCIPAL,
        [
            menu_restaurantes,
            menu_clientes,
            menu_mesas,
            menu_reservas,
            lambda: menu_usuarios(usuario),
        ],
    )
