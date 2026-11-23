# Sistema de Reservas de Restaurante

Aplicación de consola en Python para gestionar restaurantes, clientes, mesas y reservas, con **login obligatorio**. Es la continuación del proyecto de la Evaluación N°2: se mantiene el modelo de datos, los scripts SQL, el diagrama de clases y el archivo `.env`, y se agrega persistencia con **Peewee**, autenticación con **Bcrypt** y contraseñas ocultas con **Maskpass**.

## Funcionalidades

- **Login obligatorio**: no se puede acceder al menú sin iniciar sesión (máximo 3 intentos).
- **CRUD completo** de restaurantes, clientes, mesas y reservas (registrar, consultar, buscar, modificar, eliminar o cancelar).
- **Gestión de usuarios**: registrar, consultar, cambiar contraseña y habilitar/deshabilitar.
- Validación de capacidad de la mesa y de disponibilidad (no se puede reservar dos veces la misma mesa en la misma fecha y hora).

## Tecnologías y dependencias

| Librería | Uso |
|---|---|
| Python 3 | Lenguaje |
| MySQL | Base de datos |
| peewee | ORM |
| pymysql | Driver de MySQL para Peewee |
| python-decouple | Lectura del archivo `.env` |
| bcrypt | Hash de contraseñas |
| maskpass | Ocultar la contraseña al escribirla |

## Estructura del proyecto

```
main.py                      # Punto de entrada: llama primero al login
.env / .env.example          # Datos de conexión (el .env no se sube al repositorio)
requirements.txt
auxiliares/                  # Validaciones, mensajes y configuración
    info_app.py
    opciones_menu.py
    validaciones.py
datos/                       # Persistencia
    conexion.py              # Conexión a MySQL con Peewee
    modelos/                 # models.py (ModelBase) + un modelo por entidad
    repositorios/            # repo_*.py: guardar, listar, buscar, eliminar
    sql/                     # Scripts de creación de la BD
negocio/                     # Reglas del sistema (negocio_*.py)
presentacion/                # Menús y entrada/salida por consola
docs/                        # Diagrama de clases y modelo de datos
```

Cada capa solo habla con la siguiente: `presentacion → negocio → datos`. Las sentencias de acceso a la BD están únicamente en los repositorios.

## Instalación

1. Tener instalado y funcionando MySQL Server.
2. Crear la base de datos y las tablas ejecutando `datos/sql/restaurante.sql` (MySQL Workbench, phpMyAdmin o consola). El script se puede volver a ejecutar sin problema: usa `IF NOT EXISTS`. Incluye la tabla `usuarios`.
3. Crear el usuario de la aplicación ejecutando `datos/sql/crear_usuario.sql` con una cuenta administradora (antes cambie `tu_contraseña` por la que usará en el `.env`). Ese usuario solo tiene permisos `SELECT`, `INSERT`, `UPDATE` y `DELETE`; la aplicación no usa `root`.
4. Instalar las dependencias desde la carpeta del proyecto:

```powershell
python -m pip install -r requirements.txt
```

5. Copiar `.env.example`, renombrar la copia como `.env` y completar los datos de conexión:

```ini
db=restaurante
host=localhost
port=3306
user=usuario_restaurante
password=tu_contraseña
```

El archivo `.env` está excluido del repositorio mediante `.gitignore`. Cada persona debe crear el suyo.

## Ejecución

Desde una terminal (PowerShell, CMD o Terminal), en la carpeta del proyecto:

```powershell
python main.py
```

> Maskpass necesita una terminal real para ocultar la contraseña. En algunos editores (por ejemplo la consola integrada de PyCharm) no funciona: ejecute el programa desde la terminal del sistema.

Primer uso: si no existen usuarios, el sistema pide crear el primer usuario antes de mostrar el login. Luego se inicia sesión con ese usuario y se accede al menú principal:

1. Gestionar restaurantes
2. Gestionar clientes
3. Gestionar mesas
4. Gestionar reservas
5. Gestionar usuarios
6. Cerrar sesión

Orden recomendado para probar: crear un restaurante → crear mesas (necesitan un restaurante) → crear clientes → registrar reservas (necesitan cliente y mesa).

## Persistencia con Peewee

- `datos/conexion.py` crea la conexión a MySQL con los datos del `.env`.
- `datos/modelos/models.py` define `ModelBase`, de la que **heredan todos los modelos** (`Restaurante`, `Cliente`, `Mesa`, `Reserva`, `Usuario`), de modo que la configuración de la BD está centralizada.
- Cada entidad tiene su repositorio en `datos/repositorios/` con funciones `guardar()` (usa `save()` para insertar y actualizar), `listar()`, `buscar_por_...()` y `eliminar()`.

## Seguridad

- Las contraseñas **nunca se guardan en texto plano**: se almacena el hash **Bcrypt** (con salt) en `usuarios.password_hash`.
- Al iniciar sesión se compara la contraseña ingresada con el hash usando `bcrypt.checkpw`.
- Al escribir una contraseña se oculta con **Maskpass** (se muestran `*`).
- El mensaje de error del login es el mismo si el usuario no existe o la contraseña es incorrecta.
- Los usuarios no se borran: se deshabilitan. No se puede deshabilitar el propio usuario ni el último activo.

## Programación orientada a objetos

- **Herencia**: todos los modelos heredan de `ModelBase` (que hereda de `peewee.Model`).
- **Polimorfismo**: cada modelo sobrescribe `mostrar_datos()`; `presentacion/entradas.py::mostrar_lista()` recibe una lista de objetos de cualquier clase y llama a `mostrar_datos()` sin saber de qué clase es.
- **Encapsulamiento**: el acceso a datos está encapsulado en los repositorios y las reglas en la capa de negocio; el `Usuario` nunca muestra su contraseña ni su hash.

## Diagramas

- Diagrama de clases (Evaluación N°3): `docs/diagrama-clases.png`
- Modelo de datos: `docs/modelo-datos.png`
- Diagrama de clases de la Evaluación N°2 (conservado): `docs/diagrama-clases-eval2.png`
