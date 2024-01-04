from bank import value

def test_hello():
    #test for the case where it begins with hello
    #test for case insensitive
    assert value('Hello, how are you') == 0
    #test for ignoring leading whitespace
    assert value('  hello, how are you') == 0

def test_h():
    assert value('hey there') == 20
    assert value(' Hey there') == 20

def test_100():
    assert value('Good day') == 100
    assert value("What's up!") == 100

def test_symbols():
    assert value('@#$') == 100
