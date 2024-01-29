# Test the functionality of gratitudes.py
from lib.gratitudes import *

def test_Gratitudes():
    new_gratitudes = Gratitudes()
    assert new_gratitudes.gratitudes == []
    assert str(new_gratitudes.format()) == 'Be grateful for: '
    new_gratitudes.add('Health')
    assert str(new_gratitudes.format()) == 'Be grateful for: Health'
    new_gratitudes.add('Happiness')
    assert str(new_gratitudes.format()) == 'Be grateful for: Health, Happiness'
