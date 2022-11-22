import src

def test_soma():
    assert src.add(1,5) == 6, "Deveria ser 6"
    assert src.add(5,8) == 13, "Deveria ser 13"
    assert src.add(10,7) == 17, "Deveria ser 17"
    assert src.add(20,54) == 74, "Deveria ser 74"

def test_sub():
    assert src.subtract(12,7) == 5, "Deveria ser 5"
    assert src.subtract(17,10) == 7, "Deveria ser 7"
    assert src.subtract(50,21) == 29, "Deveria ser 39"
    assert src.subtract(31,2) == 29, "Deveria ser 29"

def test_mult():
    assert src.multiply(1,5) == 5, "Deveria ser 5"
    assert src.multiply(14,2) == 28, "Deveria ser 28"
    assert src.multiply(10,7) == 70, "Deveria ser 70"
    assert src.multiply(20,4) == 80, "Deveria ser 80"

def test_checkid():
    assert src.checkid('1') == 1, "Deveria ser 1"
    assert src.checkid('2') == 1, "Deveria ser 1"
    assert src.checkid('3') == 1, "Deveria ser 1"
    assert src.checkid('10') == 0, "Deveria ser 0"

def test_continuecalc():
    assert src.continuecalc("sim") == 1, "Deveria ser 1"
    assert src.continuecalc("nao") == 0, "Deveria ser 0"
    assert src.continuecalc("daada") == -1, "Deveria ser -1"

def test_calcgeral():
    assert src.calcgeral("1", 5, 8, 'nao') == 13, "Deveria ser 13" 
