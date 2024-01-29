# Tests the functionality of the greet.py functions
from lib.greet import *

def test_greet():
    result = greet('Test Name')
    assert result == 'Hello, Test Name!'