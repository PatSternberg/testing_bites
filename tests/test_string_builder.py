# Test the functionality of string_builder.py
from lib.string_builder import *

def test_StringBuilder():
    new_string_builder = StringBuilder()
    new_string_builder.add('5Char')
    result1 = new_string_builder.size()
    result2 = new_string_builder.output()
    new_string_builder.add(' 5MrC')
    result3 = new_string_builder.size()
    result4 = new_string_builder.output()
    assert result1 == 5
    assert result2 == '5Char'
    assert result3 == 10
    assert result4 == '5Char 5MrC'