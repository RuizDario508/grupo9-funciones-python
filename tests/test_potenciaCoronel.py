from funciones.potenciaCoronel import potencia_coronel

def test_potencia_coronel():
    assert potencia_coronel(2, 3) == 8
    assert potencia_coronel(5, 0) == 1
    assert potencia_coronel(-2, 3) == -8
