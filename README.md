# Sistema de Reservas de Restaurante

## Descripción

Sistema de gestión de reservas de restaurante desarrollado en Python, utilizando programación orientada a objetos (POO), arquitectura modular y una base de datos MySQL.

Permite administrar clientes, mesas y reservas mediante una interfaz de consola.

## Funcionalidades

### Gestión de clientes
- Registrar clientes.
- Consultar clientes.
- Modificar información de clientes.
- Eliminar clientes.

### Gestión de mesas
- Registrar mesas.
- Consultar mesas.
- Modificar mesas.
- Eliminar mesas.

### Gestión de reservas
- Registrar reservas.
- Consultar reservas.
- Modificar reservas.
- Cancelar reservas.
- Comprobar la capacidad de las mesas.
- Comprobar disponibilidad para evitar reservas simultáneas en una misma mesa.

## Tecnologías utilizadas

- Python 3
- MySQL
- PyMySQL
- python-decouple
- Git y GitHub

## Estructura del proyecto

- `datos/modelos/`: clases del sistema.
- `datos/repositorio/`: operaciones SQL.
- `datos/conexion/`: conexión con MySQL.
- `datos/sql/`: scripts SQL.
- `negocio/`: lógica de gestión de reservas.
- `presentacion/`: menús de consola.
- `sistema-reservas.py`: archivo principal.

## Preparación de MySQL

1. Tener instalado y funcionando MySQL Server.
2. Abrir MySQL Workbench, phpMyAdmin o un cliente de MySQL.
3. Ejecutar `datos/sql/restaurante.sql` para crear la base de datos `restaurante` y sus tablas.
4. Ejecutar `datos/sql/crear_usuario.sql` mediante una cuenta con permisos de administración.

El usuario de la aplicación se denomina `usuario_restaurante` y tiene únicamente los permisos `SELECT`, `INSERT`, `UPDATE` y `DELETE` sobre la base de datos `restaurante`.

La aplicación no utiliza la cuenta `root` para conectarse.

## Instalación de dependencias

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

```powershell
python -m pip install pymysql python-decouple
```

## Configuración de conexión

1. Copiar el archivo `.env.example`.
2. Renombrar la copia como `.env`.
3. Configurar los datos de conexión:

```ini
db=restaurante
host=localhost
port=3306
user=usuario_restaurante
password=RestauranteLocal2026!
```

La contraseña debe coincidir con la configurada para ese usuario en MySQL.

El archivo `.env` contiene credenciales locales y está excluido del repositorio mediante `.gitignore`.

Cada persona que descargue el proyecto debe configurar su propia conexión local.

## Ejecución del sistema

Desde la carpeta principal del proyecto ejecutar:

```powershell
python .\sistema-reservas.py
```

Aparecerá el menú principal:

1. Gestionar clientes.
2. Gestionar mesas.
3. Gestionar reservas.
4. Salir.

Para registrar mesas debe existir previamente un restaurante en la tabla `restaurantes`. Para registrar reservas deben existir clientes y mesas.

## Programación orientada a objetos

El proyecto incluye clases como `Cliente`, `Mesa`, `Reserva` y `Restaurante`.

Se implementan conceptos de programación orientada a objetos como herencia, encapsulamiento y polimorfismo.

## Diagrama UML

El diagrama UML del sistema se encuentra en la carpeta principal del repositorio.

