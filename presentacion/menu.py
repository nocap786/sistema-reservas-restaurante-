from datos.repositorio.cliente_repositorio import (
    registrar_cliente,
    consultar_clientes,
    modificar_cliente,
    eliminar_cliente
)

from datos.repositorio.mesa_repositorio import (
    registrar_mesa,
    consultar_mesas,
    modificar_mesa,
    eliminar_mesa
)

from datos.repositorio.reserva_repositorio import (
    registrar_reserva,
    consultar_reservas,
    modificar_reserva,
    cancelar_reserva
)
































def menu_clientes():
    while True:
        print("\n==================================")
        print("     GESTION DE CLIENTES    ")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Consultar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menu principal")
        print("====================================")
        print("")

        opcion = input("Seleccione una opción: ")



        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")

            registrar_cliente(nombre, telefono, correo)
            print("Cliente registrado correctamente.")



        elif opcion == "2":
            clientes = consultar_clientes()

            if clientes:
             for cliente in clientes:
                print(cliente)
            else:
                print("No hay clientes registrados.")


        elif opcion == "3":
            id_cliente = int(input("ID del cliente a modificar: "))
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo telefono: ")
            correo = input("Nuevo correo: ")

            if modificar_cliente(id_cliente, nombre, telefono, correo):
                print("Cliente modificado correctamente.")
            else:
                print("No se encontro el cliente.")



        elif opcion == "4":
            id_cliente = int(input("ID del cliente a eliminar: "))
            confirmar = input("¿Seguro que desea eliminarlo? (s/n): ")

            if confirmar.lower() == "s":
                if eliminar_cliente(id_cliente):
                    print("Cliente eliminado correctamente.")
                else:
                    print("No se encontro el cliente.")




        elif opcion == "5":
            break

        else:
            print("Opcion no valida. Intente nuevamente.")           



def menu_mesas():
    while True:
        print("\n==================================")
        print("     GESTION DE MESAS")
        print("====================================")
        print("1. Registrar mesa")
        print("2. Consultar mesas")
        print("3. Modificar mesa")
        print("4. Eliminar mesa")
        print("5. Volver al menu principal")
        print("====================================")
        print("")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Numero de mesa: "))
            capacidad = int(input("Capacidad: "))
            caracteristicas = input("Caracteristicas: ")
            id_restaurante = int(input("ID del restaurante: "))

            registrar_mesa(numero, capacidad, caracteristicas, id_restaurante)
            print("Mesa registrada correctamente.")

        elif opcion == "2":
            mesas = consultar_mesas()

            print("\n========== MESAS REGISTRADAS ==========")

            if mesas:
                for mesa in mesas:
                    print(f"ID: {mesa[0]}")
                    print(f"Numero: {mesa[1]}")
                    print(f"Capacidad: {mesa[2]}")
                    print(f"Caracteristicas: {mesa[3]}")
                    print(f"Restaurante: {mesa[4]}")
                    print("----------------------------------")
            else:
                print("No hay mesas registradas.")

            input("\nPresione Enter para volver...")

        elif opcion == "3":
            id_mesa = int(input("ID de la mesa a modificar: "))
            numero = int(input("Nuevo numero: "))
            capacidad = int(input("Nueva capacidad: "))
            caracteristicas = input("Nuevas caracteristicas: ")

            if modificar_mesa(id_mesa, numero, capacidad, caracteristicas):
                print("Mesa modificada correctamente.")
            else:
                print("No se encontro la mesa.")

        elif opcion == "4":
            id_mesa = int(input("ID de la mesa a eliminar: "))
            confirmar = input("¿Seguro que desea eliminarla? (s/n): ")

            if confirmar.lower() == "s":
                if eliminar_mesa(id_mesa):
                    print("Mesa eliminada correctamente.")
                else:
                    print("No se encontro la mesa.")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida. Intente nuevamente.")



def menu_reservas():
    while True:
        print("\n==================================")
        print("       GESTION DE RESERVAS")
        print("==================================")
        print("1. Registrar reserva")
        print("2. Consultar reservas")
        print("3. Modificar reserva")
        print("4. Cancelar reserva")
        print("5. Volver al menu principal")
        print("==================================")
        print("")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_cliente = int(input("ID del cliente: "))
                id_mesa = int(input("ID de la mesa: "))
                fecha = input("Fecha (AAAA-MM-DD): ")
                hora = input("Hora (HH:MM): ")
                cantidad_personas = int(input("Cantidad de personas: "))

                if registrar_reserva(id_cliente, id_mesa, fecha, hora, cantidad_personas):
                    print("Reserva registrada correctamente.")
                else:
                    print("No se pudo reservar. Revise la capacidad y disponibilidad.")
            except ValueError:
                print("Datos invalidos. Intente nuevamente.")

        elif opcion == "2":
            reservas = consultar_reservas()

            print("\n========== RESERVAS REGISTRADAS ==========")
            if reservas:
                for reserva in reservas:
                    print(f"ID: {reserva[0]}")
                    print(f"Cliente: {reserva[1]}")
                    print(f"Mesa: {reserva[2]}")
                    print(f"Fecha: {reserva[3]}")
                    print(f"Hora: {reserva[4]}")
                    print(f"Personas: {reserva[5]}")
                    print(f"Estado: {reserva[6]}")
                    print("----------------------------------")
            else:
                print("No hay reservas registradas.")

            input("\nPresione Enter para volver...")

        elif opcion == "3":
            try:
                id_reserva = int(input("ID de la reserva: "))
                fecha = input("Nueva fecha (AAAA-MM-DD): ")
                hora = input("Nueva hora (HH:MM): ")
                personas = int(input("Nueva cantidad de personas: "))

                if modificar_reserva(id_reserva, fecha, hora, personas):
                    print("Reserva modificada correctamente.")
                else:
                    print("No se pudo modificar la reserva.")
            except ValueError:
                print("Datos invalidos. Intente nuevamente.")

        elif opcion == "4":
            try:
                id_reserva = int(input("ID de la reserva a cancelar: "))
                confirmar = input("¿Confirmar cancelacion? (s/n): ")

                if confirmar.lower() == "s":
                    if cancelar_reserva(id_reserva):
                        print("Reserva cancelada correctamente.")
                    else:
                        print("No se encontro una reserva activa.")
            except ValueError:
                print("ID invalido.")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida. Intente nuevamente.")
