from auxiliares.info_app import (
    MSG_DESPEDIDA,
    MSG_ERROR_CONEXION,
    MSG_ERROR_INESPERADO,
    MSG_SESION_INTERRUMPIDA,
)


def main():
    try:
        from datos.conexion import cerrar, conectar

        conectar()
    except Exception as error:
        print(MSG_ERROR_CONEXION.format(error))
        return

    try:
        from presentacion.menu import menu_principal
        from presentacion.presentacion_usuario import iniciar_sesion

        # El login es obligatorio: sin usuario autenticado no se abre el menu.
        usuario = iniciar_sesion()
        if usuario is not None:
            menu_principal(usuario)
    except KeyboardInterrupt:
        print(f"\n{MSG_SESION_INTERRUMPIDA}")
    except Exception as error:
        print(MSG_ERROR_INESPERADO.format(error))
    finally:
        cerrar()

    print(MSG_DESPEDIDA)


if __name__ == "__main__":
    main()
