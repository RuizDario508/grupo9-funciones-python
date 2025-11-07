# tests/test_raiz_cuadrada_soto.py
from funciones.raiz_cuadrada_soto import raiz_cuadrada

def test_raiz_cuadrada_positiva():
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(0) == 0
    assert raiz_cuadrada(2.25) == 1.5

def test_raiz_cuadrada_negativa():
    assert raiz_cuadrada(-4) is None

def test_raiz_cuadrada_none():
    assert raiz_cuadrada(None) is None

