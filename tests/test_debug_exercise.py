from lib.debug_exercise import *

def test_get_most_common_letter():
    test_var = 'the roof, the roof, the roof is on fire!'
    assert get_most_common_letter(test_var) == 'o'
