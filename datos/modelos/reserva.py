class Reserva:
    def __init__(self, id_reserva, cliente, mesa, fecha, hora, cantidad_personas, estado="Pendiente"):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.mesa = mesa
        self.fecha = fecha
        self.hora = hora
        self.cantidad_personas = cantidad_personas
        self.estado = estado

    def mostrar_datos(self):
        print(f"ID Reserva: {self.id_reserva}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Mesa: {self.mesa.numero}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Personas: {self.cantidad_personas}")
        print(f"Estado: {self.estado}")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado