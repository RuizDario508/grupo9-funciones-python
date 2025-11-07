from funciones.es_par_segovia import es_par_segovia

def test_es_par_segovia():
    assert es_par_segovia(4) is True
    assert es_par_segovia(7) is False



