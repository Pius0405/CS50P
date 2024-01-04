from seasons import validate_dob, get_word, get_minutes
import datetime
import pytest

def test_validate_dob():
    assert validate_dob("2004-05-04") == True
    assert validate_dob("February 6th, 1998") == False


