from twttr import shorten

def test_NoVowel():
    assert shorten('dry') == 'dry'
    assert shorten('Fly') == 'Fly'

def test_Vowel():
    #lowercase vowel replacement
    assert shorten('Hello') == 'Hll'
    assert shorten('twitter') == 'twttr'
    #uppercase vowel replacement
    assert shorten('WORLD') == 'WRLD'

def test_numbers():
    assert shorten('123') == '123'
    assert shorten('cs50') == 'cs50'

def test_symbols():
    assert shorten('@#$') == '@#$'
    assert shorten('$100') == '$100'
    assert shorten('Hello!') == 'Hll!'
