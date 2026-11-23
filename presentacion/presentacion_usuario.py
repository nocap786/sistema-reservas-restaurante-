from auxiliares.info_app import (
    MAX_INTENTOS_LOGIN,
    MSG_BIENVENIDA,
    MSG_LOGIN_BLOQUEADO,
    MSG_PASSWORDS_DISTINTAS,
    MSG_PRIMER_USUARIO,
)
from auxiliares.opciones_menu import MENU_USUARIOS
from negocio import negocio_usuarios
from presentacion.entradas import (
    ejecutar_menu,
    mostrar_lista,
    mostrar_resultado,
    pedir_entero,
    pedir_password,
    pedir_texto,
)


def _pedir_password_confirmada(mensaje="Contraseña: "):
    """Pide la contraseña dos veces (oculta con Maskpass). None si no coinciden."""
    password = pedir_password(mensaje)
    repeticion = pedir_password("Repita la contraseña: ")
    if password != repeticion:
        print(MSG_PASSWORDS_DISTINTAS)
        return None
    return password


def _registrar_usuario():
    """Registra un usuario. Devuelve True si se creo."""
    nombre = pedir_texto("Nombre de usuario: ")
    password = _pedir_password_confirmada()
    if password is None:
        return False
    resultado = negocio_usuarios.registrar_usuario(nombre, password)
    mostrar_resultado(resultado)
    return resultado[0]


def iniciar_sesion():
    """Login obligatorio. Devuelve el Usuario autenticado o None."""
    if negocio_usuarios.no_hay_usuarios():
        print(MSG_PRIMER_USUARIO)
        while not _registrar_usuario():
            pass

    for _ in range(MAX_INTENTOS_LOGIN):
        print("\n--- INICIO DE SESION ---")
        nombre = pedir_texto("Usuario: ")
        password = pedir_password("Contraseña: ")
        ok, mensaje, usuario = negocio_usuarios.autenticar(nombre, password)
        if ok:
            print(MSG_BIENVENIDA.format(usuario.nombre_usuario))
            return usuario
        print(mensaje)

    print(MSG_LOGIN_BLOQUEADO)
    return None


def menu_usuarios(usuario_actual):
    def _consultar():
        mostrar_lista("USUARIOS", negocio_usuarios.listar_usuarios(), "usuarios")

    def _cambiar_password():
        id_usuario = pedir_entero("ID del usuario: ", minimo=1)
        password = _pedir_password_confirmada("Nueva contraseña: ")
        if password is not None:
            mostrar_resultado(negocio_usuarios.cambiar_password(id_usuario, password))

    def _cambiar_estado():
        id_usuario = pedir_entero("ID del usuario: ", minimo=1)
        activo = pedir_texto("¿Habilitar (h) o deshabilitar (d)?: ").lower() == "h"
        mostrar_resultado(
            negocio_usuarios.cambiar_estado(id_usuario, activo, usuario_actual.id_usuario)
        )

    ejecutar_menu(
        "GESTION DE USUARIOS",
        MENU_USUARIOS,
        [_registrar_usuario, _consultar, _cambiar_password, _cambiar_estado],
    )
