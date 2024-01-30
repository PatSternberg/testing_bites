# Test the present.py file
import pytest
from lib.present import *

def test_present_wrap_success():
    present = Present()
    present.wrap('Gift')
    assert present.contents == 'Gift'

def test_present_wrap_error():
    present = Present()
    present.wrap('Gift')
    with pytest.raises(Exception) as new_error:
        present.wrap('AnotherGift')
    error_message = str(new_error.value)
    assert error_message == 'A contents has already been wrapped.'

def test_present_unwrap_success():
    present = Present()
    present.wrap('Gift')
    assert present.unwrap() == 'Gift'

def test_present_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as new_error:
        present.unwrap()
    error_message = str(new_error.value)
    assert error_message == 'No contents have been wrapped.'