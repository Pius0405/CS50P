from project import get_move, check_21, check_busted

def test_get_move():
    #input H when testing
    assert get_move(12) == "H"

def test_check_21():
    assert check_21(21) == True
    assert check_21(17) == False

def test_check_busted():
    assert check_busted(30) == True
    assert check_busted(15) == False
