from um import count
import pytest

def test_got_um():
    assert count('Um, thanks, um...') == 2
    assert count('um, let me think') == 1

def test_no_um():
    assert count("I'm not sure") == 0
    assert count('yes it is') == 0

def test_um_in_word():
    assert count('A yummy ectobacterium') == 0
    assert count("Um,...It's um.... semidocumentary") == 2
