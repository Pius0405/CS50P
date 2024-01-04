from fuel import convert, gauge

import pytest

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'

def test_convert():
    assert convert('1/2') == 50
    # expect convert() to raise ZeroDivisionError
    #test for denominator = 0
    with pytest.raises(ZeroDivisionError):
        convert('5/0')
    #test for non-numeric string
    with pytest.raises(ValueError):
        convert('cat/dog')
    #test for improper function
    with pytest.raises(ValueError):
        convert('5/3')



