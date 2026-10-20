from datos.conexion.conexion_bd import conectar_bd


def registrar_reserva(id_cliente, id_mesa, fecha, hora, cantidad_personas):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT capacidad FROM mesas
                WHERE id_mesa = %s
            """, (id_mesa,))
            mesa = cursor.fetchone()

            if not mesa or cantidad_personas < 1 or cantidad_personas > mesa[0]:
                return False

            cursor.execute("""
                SELECT id_reserva FROM reservas
                WHERE id_mesa = %s AND fecha = %s AND hora = %s
                AND estado IN ('Pendiente', 'Confirmada')
            """, (id_mesa, fecha, hora))

            if cursor.fetchone():
                return False

            cursor.execute("""
                INSERT INTO reservas
                (id_cliente, id_mesa, fecha, hora, cantidad_personas, estado)
                VALUES (%s, %s, %s, %s, %s, 'Pendiente')
            """, (id_cliente, id_mesa, fecha, hora, cantidad_personas))

        conexion.commit()
        return True
    finally:
        conexion.close()


def consultar_reservas():
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT r.id_reserva, c.nombre, m.numero,
                       r.fecha, r.hora, r.cantidad_personas, r.estado
                FROM reservas r
                JOIN clientes c ON r.id_cliente = c.id_cliente
                JOIN mesas m ON r.id_mesa = m.id_mesa
                ORDER BY r.fecha, r.hora
            """)
            return cursor.fetchall()
    finally:
        conexion.close()


def modificar_reserva(id_reserva, fecha, hora, cantidad_personas):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT r.id_mesa, m.capacidad
                FROM reservas r
                JOIN mesas m ON r.id_mesa = m.id_mesa
                WHERE r.id_reserva = %s AND r.estado != 'Cancelada'
            """, (id_reserva,))
            reserva = cursor.fetchone()

            if not reserva or cantidad_personas < 1 or cantidad_personas > reserva[1]:
                return False

            cursor.execute("""
                SELECT id_reserva FROM reservas
                WHERE id_mesa = %s AND fecha = %s AND hora = %s
                AND estado IN ('Pendiente', 'Confirmada')
                AND id_reserva != %s
            """, (reserva[0], fecha, hora, id_reserva))

            if cursor.fetchone():
                return False

            cursor.execute("""
                UPDATE reservas
                SET fecha = %s, hora = %s, cantidad_personas = %s
                WHERE id_reserva = %s
            """, (fecha, hora, cantidad_personas, id_reserva))
            filas = cursor.rowcount

        conexion.commit()
        return filas > 0
    finally:
        conexion.close()


def cancelar_reserva(id_reserva):
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE reservas SET estado = 'Cancelada'
                WHERE id_reserva = %s AND estado != 'Cancelada'
            """, (id_reserva,))
            filas = cursor.rowcount

        conexion.commit()
        return filas > 0
    finally:
        conexion.close()