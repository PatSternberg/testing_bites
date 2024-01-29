# Test the functionality of counter.py
from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(5)
    result1 = counter.report()
    counter.add(10)
    result2 = counter.report()
    assert result1 == "Counted to 5 so far."
    assert result2 == "Counted to 15 so far."
