# Tests the functionality of the test in check_codeword.py
from lib.check_codeword import *

def test_check_codeword():
    result1 = check_codeword('TotallyWrong')
    result2 = check_codeword('hAlmostCorrecte')
    result3 = check_codeword('horse')

    assert result1 == 'WRONG!'
    assert result2 == 'Close, but nope.'
    assert result3 == 'Correct! Come in.'


    # if codeword == "horse":
    #     return "Correct! Come in."
    # elif codeword[0] == "h" and codeword[-1] == "e":
    #     return "Close, but nope."
    # else:
    #     return "WRONG!"