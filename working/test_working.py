from working import convert
import pytest


def test_valid_time():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'


def test_wrong_format():
    with pytest.raises(ValueError):
        convert('08:00 to 17:00')
    with pytest.raises(ValueError):
        convert('cats:dogs to 17:00')
    with pytest.raises(ValueError):
        convert('7 AM - 6 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

def test_wrong_value():
    with pytest.raises(ValueError):
        convert('7:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('8.0:00 to 17:00')

