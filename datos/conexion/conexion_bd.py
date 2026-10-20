import pymysql
from decouple import config

def conectar_bd():
    return pymysql.connect(
        host=config("host", default="localhost"),
        port=config("port", default=3306, cast=int),
        user=config("user"),
        password=config("password"),
        database=config("db"),
        charset="utf8mb4"
    )