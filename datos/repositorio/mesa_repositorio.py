from datos.conexion.conexion_bd import conectar_bd


def registrar_mesa(numero, capacidad, caracteristicas, id_restaurante):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO mesas (numero, capacidad, caracteristicas, id_restaurante)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (numero, capacidad, caracteristicas, id_restaurante))
        conexion.commit()
        return True
    finally:
        conexion.close()


def consultar_mesas():
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id_mesa, numero, capacidad, caracteristicas, id_restaurante
                FROM mesas
            """)
            return cursor.fetchall()
    finally:
        conexion.close()


def modificar_mesa(id_mesa, numero, capacidad, caracteristicas):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            sql = """
                UPDATE mesas
                SET numero = %s, capacidad = %s, caracteristicas = %s
                WHERE id_mesa = %s
            """
            cursor.execute(sql, (numero, capacidad, caracteristicas, id_mesa))
            filas = cursor.rowcount
        conexion.commit()
        return filas > 0
    finally:
        conexion.close()


def eliminar_mesa(id_mesa):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM mesas WHERE id_mesa = %s",
                (id_mesa,)
            )
            filas = cursor.rowcount
        conexion.commit()
        return filas > 0
    finally:
        conexion.close()