from tasks import somar, fatorial

def test_soma():
    resultado = somar.apply(args=[5,3]).get()
    assert resultado == 8

def test_fatorial():
    resultado = fatorial.apply(args=[5]).get()
    assert resultado == 120