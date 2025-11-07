# funciones/raiz_cuadrada.py
import math

def raiz_cuadrada(x):
    """Devuelve la raíz cuadrada de un número no negativo.
    Si x < 0 devuelve None.
    """
    if x is None:
        return None
    if x < 0:
        return None
    return math.sqrt(x)
