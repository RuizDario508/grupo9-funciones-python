#tests/test_sumavargas.py
from funciones.sumavargas import sumar

def test_sumar():
    assert sumar(3, 5) == 8
    assert sumar(-2, 2) == 0 