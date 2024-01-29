# Test the functionality of the report_length.py file
from lib.report_length import *

def test_report_length():
    result1 = report_length('C++')
    result2 = report_length('Python')
    result3 = report_length('JavaScript')
    
    assert result1 == "This string was 3 characters long."
    assert result2 == "This string was 6 characters long."
    assert result3 == "This string was 10 characters long."