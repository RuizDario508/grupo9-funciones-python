from funciones.restar_medina import restar_medina

def test_restar_medina():
    assert restar_medina(10, 4) == 6
    assert restar_medina(5, 10) == -5
