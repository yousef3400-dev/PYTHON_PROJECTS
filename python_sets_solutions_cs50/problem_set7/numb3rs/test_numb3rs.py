from numb3rs import validate


def test_validate():
    assert validate("200.2.2.2") == True
    assert validate("200.2.4.2") == True
    assert validate("200.1.2.2") == True
    assert validate("210.2.2.2") == True

def test_not_validate():
    assert validate("700.2.2.2") == False
    assert validate("200.1.272.2") == False
    assert validate("210.2.-1.2") == False
    assert validate("200.2.302.2") == False
