from funciones.PotenciaCoronel import Potencia_Coronel

def test_Potencia_Coronel():
    assert Potencia_Coronel(2, 3) == 8
    assert Potencia_Coronel(5, 0) == 1
    assert Potencia_Coronel(-2, 3) == -8
