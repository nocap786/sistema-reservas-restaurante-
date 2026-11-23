"""Validaciones reutilizables. No interactuan con el usuario ni con la BD."""

import re
from datetime import datetime

from auxiliares.info_app import MAX_BYTES_PASSWORD, MIN_LARGO_PASSWORD


def texto_valido(texto, maximo=100):
    """Texto no vacio y que no supera el largo maximo."""
    return bool(texto and texto.strip()) and len(texto.strip()) <= maximo


def correo_valido(correo):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo or ""))


def parsear_fecha(texto):
    """Devuelve un date a partir de 'AAAA-MM-DD', o None si es invalida."""
    try:
        return datetime.strptime(texto.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def parsear_hora(texto):
    """Devuelve un time a partir de 'HH:MM', o None si es invalida."""
    try:
        return datetime.strptime(texto.strip(), "%H:%M").time()
    except ValueError:
        return None


def nombre_usuario_valido(nombre):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", nombre or ""))


def password_valida(password):
    if password is None:
        return False
    return (
        len(password) >= MIN_LARGO_PASSWORD
        and len(password.encode("utf-8")) <= MAX_BYTES_PASSWORD
    )
