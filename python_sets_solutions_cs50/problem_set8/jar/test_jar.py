import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5

    jar = Jar(0)
    assert jar.capacity == 0

    for bad in [-1, "5", 2.5, None, True]:
        with pytest.raises(ValueError):
            Jar(bad)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(7)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(1)
    assert jar.size == 10  # الحالة متتغيرتش بعد الخطأ

    with pytest.raises(ValueError):
        Jar().deposit(13)

    with pytest.raises(ValueError):
        Jar().deposit(-1)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)
    assert jar.size == 0

    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_capacity_and_size_are_read_only():
    jar = Jar()
    with pytest.raises(AttributeError):
        jar.capacity = 20
    with pytest.raises(AttributeError):
        jar.size = 5
