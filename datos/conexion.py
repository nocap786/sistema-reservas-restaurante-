"""Conexion a MySQL mediante Peewee. Los datos salen del archivo .env."""

from decouple import config
from peewee import MySQLDatabase

db = MySQLDatabase(
    config("db"),
    host=config("host", default="localhost"),
    port=config("port", default=3306, cast=int),
    user=config("user"),
    password=config("password"),
    charset="utf8mb4",
)


def conectar():
    if db.is_closed():
        db.connect()


def cerrar():
    if not db.is_closed():
        db.close()
