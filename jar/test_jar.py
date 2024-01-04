from jar import Jar
import pytest


def test_init():
    #create jar objects to test jar.py
    #jar with default capacity
    jar1 = Jar()
    assert jar1.capacity == 12
    #jar with capacity of 10
    jar2 = Jar(10)
    assert jar2.capacity == 10
    with pytest.raises(ValueError):
        Jar(-10)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar()
    jar1.deposit(5)
    assert jar1.size == 5
    with pytest.raises(ValueError):
        jar1.deposit(20)


def test_withdraw():
    jar1 = Jar()
    jar1.deposit(5)
    jar1.withdraw(2)
    assert jar1.size == 3
    with pytest.raises(ValueError):
        jar1.withdraw(10)

