import pytest
from numb3rs import validate

def test_validIP():
    assert validate('255.123.0.19') == True
    #test for corner cases i.e. 255, 0
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True

def test_wordIP():
    assert validate('cat') == False

def test_invalid_format_IP():
    assert validate('255.1') == False
    assert validate('16.18.98.77.65') == False
    assert validate('127.300.1.2') == False
