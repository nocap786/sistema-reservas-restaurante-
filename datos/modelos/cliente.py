class Persona:
    def __init__(self, nombre, telefono, correo):
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo

    def mostrar_datos(self):
        print(f"Nombre: {self._nombre}")
        print(f"Telefono: {self._telefono}")
        print(f"Correo: {self._correo}")


class Cliente(Persona):
    def __init__(self, id_cliente, nombre, telefono, correo):
        super().__init__(nombre, telefono, correo)
        self._id_cliente = id_cliente

    def mostrar_datos(self):
        print(f"ID: {self._id_cliente}")
        super().mostrar_datos()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nuevo_nombre


        
