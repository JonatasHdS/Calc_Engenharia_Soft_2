import src

def test_soma():
    assert add(1,5) == 6, "Deveria ser 6"
    assert add(5,8) == 13, "Deveria ser 13"
    assert add(10,7) == 17, "Deveria ser 17"
    assert add(20,54) == 74, "Deveria ser 74"

def test_sub():
    assert subtract(12,7) == 5, "Deveria ser 5"
    assert subtract(17,10) == 7, "Deveria ser 7"
    assert subtract(50,21) == 39, "Deveria ser 39"
    assert subtract(31,2) == 29, "Deveria ser 29"

def test_mult():
    assert multiply(1,5) == 5, "Deveria ser 5"
    assert multiply(14,2) == 28, "Deveria ser 28"
    assert multiply(10,7) == 70, "Deveria ser 70"
    assert multiply(20,4) == 100, "Deveria ser 100"

def test_div():
    assert add(18,2) == 9, "Deveria ser 9"
    assert add(12,3) == 4, "Deveria ser 4"
    assert add(50,5) == 10, "Deveria ser 10"
    assert add(60,3) == 20, "Deveria ser 20" 

def test_checkid():
    assert checkid('1') == 1, "Deveria ser 1"
    assert checkid('2') == 1, "Deveria ser 1"
    assert checkid('3') == 1, "Deveria ser 1"
    assert checkid('10') == 0, "Deveria ser 0"

def test_continuecalc():
    assert continuecalc("sim") == 1, "Deveria ser 1"
    assert continuecalc("nao") == 0, "Deveria ser 0"
    assert continuecalc("daada") == -1, "Deveria ser -1"

def test_calcgeral():
    assert calcgeral("1", 5, 8, 'nao') == 13, "Deveria ser 13" 
