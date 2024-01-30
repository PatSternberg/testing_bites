from lib.debug_practice import *

def test_say_hello():
    result = say_hello('kay')
    assert result == 'hello kay'

def test_encode():
    assert encode('theswiftfoxjumpedoverthelazydog', 'secretkey') == 'EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL'

def test_decode():
    assert decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey') == 'theswiftfoxjumpedoverthelazydog'