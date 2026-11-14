from bank import value


def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0


def test_value_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20
    assert value("h") == 20


def test_value_other():
    assert value("goodbye") == 100
    assert value("greetings") == 100
    assert value("") == 100


def test_value_whitespace():
    assert value(" hello") == 0
    assert value("   hey") == 20
    assert value("   goodbye") == 100
