from funciones.PotenciaCoronel import PotenciaCoronel  

def test_potencia_coronel():
    assert PotenciaCoronel(2, 3) == 8
    assert PotenciaCoronel(5, 0) == 1
    assert PotenciaCoronel(-2, 3) == -8
