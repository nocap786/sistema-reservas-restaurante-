import os
import pymysql


def conectar_bd():
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=os.environ["MYSQL_PASSWORD"],
        database="restaurante",
        charset="utf8mb4"
    )
    return conexion