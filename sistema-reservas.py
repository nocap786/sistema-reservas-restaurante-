from presentacion.menu import menu_clientes, menu_mesas, menu_reservas



from datos.repositorio.reserva_repositorio import (
    registrar_reserva,
    consultar_reservas,
    modificar_reserva,
    cancelar_reserva
)



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






def iniciar_sistema():
    while True:
        print("\n===================================")
        print("  SISTEMA DE RESERVAS RESTAURANTE"   )
        print("==================================")
        print("1. Gestionar clientes")
        print("2. Gestionar mesas")
        print("3. Gestionar reservas")
        print("4. Salir")
        print("==================================")
        print("")

        opcion = input("Selecione una opción: ")

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




     






































          










