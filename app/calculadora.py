"""Este módulo calculadora"""

# app/calculadora.py


def sumar(a, b):
    """Operación suma"""
    return a + b


def restar(a, b):
    """Operación resta"""
    return a - b


def multiplicar(a, b):
    """Operación multiplicar"""
    return a * b


def dividir(a, b):
    """Operación dividir"""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
