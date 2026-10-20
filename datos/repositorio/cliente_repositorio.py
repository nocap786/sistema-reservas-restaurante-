from datos.conexion.conexion_bd import conectar_bd


def registrar_cliente(nombre, telefono, correo):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO clientes (nombre, telefono, correo)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (nombre, telefono, correo))
        conexion.commit()
        return True
    finally:
        conexion.close()


def consultar_clientes():
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT id_cliente, nombre, telefono, correo FROM clientes"
            )
            return cursor.fetchall()
    finally:
        conexion.close()


def modificar_cliente(id_cliente, nombre, telefono, correo):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            sql = """
                UPDATE clientes
                SET nombre = %s, telefono = %s, correo = %s
                WHERE id_cliente = %s
            """
            cursor.execute(sql, (nombre, telefono, correo, id_cliente))
            filas = cursor.rowcount
        conexion.commit()
        return filas > 0
    finally:
        conexion.close()


def eliminar_cliente(id_cliente):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente,))
            filas = cursor.rowcount
        conexion.commit()
        return filas > 0
    finally:
        conexion.close()