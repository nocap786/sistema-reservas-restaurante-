
from presentacion.menu import menu_clientes, menu_mesas, menu_reservas


def iniciar_sistema():
    while True:
        print("\n===================================")
        print("  SISTEMA DE RESERVAS RESTAURANTE")
        print("==================================")
        print("1. Gestionar clientes")
        print("2. Gestionar mesas")
        print("3. Gestionar reservas")
        print("4. Salir")
        print("==================================")
        print("")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            menu_mesas()

        elif opcion == "3":
            menu_reservas()

        elif opcion == "4":
            print("Cerrando el sistema...")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    iniciar_sistema()
