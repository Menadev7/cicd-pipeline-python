"""Este módulo calculadora"""
# app/calculadora.py
  """example"""
def sumar(a, b):
    return a + b


  """example"""
def restar(a, b):
    return a - b


  """example"""
def multiplicar(a, b):
    return a * b


  """example"""
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
