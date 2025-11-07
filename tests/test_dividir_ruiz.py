import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones.dividir_ruiz import dividir
def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(5, 0) is None
