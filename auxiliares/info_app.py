"""Configuracion y mensajes generales de la aplicacion."""

APP_NOMBRE = "SISTEMA DE RESERVAS DE RESTAURANTE"
APP_VERSION = "3.0"

# Configuracion
MAX_INTENTOS_LOGIN = 3
MIN_LARGO_PASSWORD = 8
MAX_BYTES_PASSWORD = 72  # limite de bcrypt

# Mensajes generales
MSG_DESPEDIDA = "Cerrando el sistema..."
MSG_OPCION_INVALIDA = "Opcion no valida. Intente nuevamente."
MSG_CAMPO_OBLIGATORIO = "Este campo es obligatorio."
MSG_ENTERO_INVALIDO = "Debe ingresar un numero entero."
MSG_FECHA_INVALIDA = "Fecha invalida. Use el formato AAAA-MM-DD."
MSG_HORA_INVALIDA = "Hora invalida. Use el formato HH:MM."
MSG_SIN_REGISTROS = "No hay {} registrados."
MSG_NO_ENCONTRADO = "No se encontro {}."
MSG_ERROR_CONEXION = "No se pudo conectar a la base de datos: {}"
MSG_ERROR_INESPERADO = "Ocurrio un error inesperado: {}"
MSG_SESION_INTERRUMPIDA = "Sesion interrumpida."

# Mensajes de login y usuarios
MSG_PRIMER_USUARIO = (
    "No existen usuarios en el sistema.\n"
    "Cree el primer usuario para poder ingresar."
)
MSG_LOGIN_FALLIDO = "Usuario o contraseña incorrectos."
MSG_LOGIN_INTENTOS = "Le quedan {} intento(s)."
MSG_LOGIN_BLOQUEADO = (
    "ACCESO DENEGADO. Demasiados intentos fallidos. Cerrando el sistema."
)
MSG_BIENVENIDA = "Bienvenido/a, {}."
MSG_PASSWORDS_DISTINTAS = "Las contraseñas no coinciden."
MSG_NOMBRE_USUARIO_INVALIDO = (
    "Nombre de usuario invalido. Use entre 3 y 30 letras, numeros o guion bajo."
)
MSG_PASSWORD_INVALIDA = (
    "Contraseña invalida. Debe tener al menos 8 caracteres "
    "(maximo 72 bytes)."
)
