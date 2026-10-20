class Reserva:
    ESTADOS_VALIDOS = ("Pendiente", "Confirmada", "Cancelada", "Completada")

    def __init__(self, id_reserva, cliente, mesa, fecha, hora, cantidad_personas, estado="Pendiente"):
        self._id_reserva = id_reserva
        self._cliente = cliente
        self._mesa = mesa
        self._fecha = fecha
        self._hora = hora
        self._cantidad_personas = cantidad_personas
        self._estado = estado

    @property
    def estado(self):
        return self._estado

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError("Estado de reserva no valido")
        self._estado = nuevo_estado

    def mostrar_datos(self):
        print(f"ID Reserva: {self._id_reserva}")
        print(f"Cliente: {self._cliente.nombre}")
        print(f"Mesa: {self._mesa.numero}")
        print(f"Fecha: {self._fecha}")
        print(f"Hora: {self._hora}")
        print(f"Personas: {self._cantidad_personas}")
        print(f"Estado: {self._estado}")