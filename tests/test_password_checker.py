import pytest
from lib.password_checker import *

def test_password_checker_success():
    password_checker = PasswordChecker()
    assert password_checker.check("AcceptablePassword") == True

def test_password_checker_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as new_error:
        password_checker.check("Fail")
    error_message = str(new_error.value)
    assert error_message == 'Invalid password, must be 8+ characters.'