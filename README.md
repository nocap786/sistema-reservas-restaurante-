Sistema de Reservas de Restaurante

Descripción

Sistema desarrollado en Python para administrar clientes, mesas y reservas de un restaurante, utilizando programación orientada a objetos (POO) y una base de datos MySQL.

Funcionalidades

Gestión de clientes

Registrar clientes.

Consultar clientes registrados.

Modificar información.

Eliminar clientes.

Gestión de mesas

Registrar mesas.

Consultar mesas.

Modificar sus características.

Eliminar mesas.

Gestión de reservas

Registrar reservas.

Consultar reservas.

Modificar fecha, hora y cantidad de personas.

Cancelar reservas.

Verificar capacidad y disponibilidad de mesas para el horario solicitado.

Tecnologías utilizadas

Python

MySQL

PyMySQL

Visual Studio Code

Git y GitHub

Organización del proyecto

datos/modelos/: clases del sistema.

datos/repositorio/: operaciones SQL y acceso a datos.

datos/conexion/: conexión a MySQL.

datos/sql/: script de creación de la base de datos.

negocio/: lógica de gestión de reservas.

presentacion/: menús e interacción con el usuario.

sistema-reservas.py: archivo principal.

Instrucciones de ejecución

Instalar Python y MySQL Server.

Crear las tablas ejecutando datos/sql/restaurante.sql en MySQL Workbench.

Instalar la dependencia:

python -m pip install pymysql

Configurar la contraseña de MySQL en la terminal PowerShell:

$env:MYSQL_PASSWORD = Read-Host "Contraseña de MySQL"

Ejecutar el programa desde la carpeta principal:

python sistema-reservas.py

La conexión está configurada para MySQL en localhost, con el usuario root y la base de datos restaurante.

Para registrar mesas debe existir previamente un restaurante en la base de datos. Para registrar reservas deben existir clientes y mesas.

Programación orientada a objetos

El proyecto incluye clases como Cliente, Mesa, Reserva y Restaurante. También incorpora ejemplos de herencia, encapsulamiento y polimorfismo.

Diagrama UML

El diagrama de clases se encuentra en la carpeta principal del repositorio.