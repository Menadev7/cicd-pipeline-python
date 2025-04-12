"""Este módulo calculadora"""
# app/calculadora.py
def sumar(a, b):
  """example"""
    return a + b


def restar(a, b):
  """example"""
    return a - b


def multiplicar(a, b):
  """example"""
    return a * b


def dividir(a, b):
  """example"""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
