from lib.most_often import *

def test_most_often_init():
    test_empty_object = MostOften([])
    assert test_empty_object.starting_list == []
    test_int_object = MostOften([-1, 0, 1, 2, 3])
    assert test_int_object.starting_list == [-1, 0, 1, 2, 3]
    test_str_object = MostOften(['One', 'Two', 'Three'])
    assert test_str_object.starting_list == ['One', 'Two', 'Three']
    test_mixed_object = MostOften([-1, 0, 'One', 2.2, 3])
    assert test_mixed_object.starting_list == [-1, 0, 'One', 2.2, 3]

def test_adds_item():
    test_obj = MostOften([])
    test_obj.add_new(4)
    assert test_obj.starting_list == [4]

def test_no_duplicates():
    test_obj = MostOften([1, 7, 1, 8, 2, 3, 5, 2, 1])
    assert test_obj.get_most_often() == 1
    test_obj = MostOften([1, 7, 1, 8, 2, 3, 5, 2, 1, 2])
    assert test_obj.get_most_often() == 'no clear winner'
    test_obj = MostOften([1, -1, 1, 2, 2])
    assert test_obj.get_most_often() != 1
    test_obj = MostOften([])
    assert test_obj.get_most_often() == 'no clear winner'
    test_obj = MostOften(['One', 'One', 'Two'])
    assert test_obj.get_most_often() == 'One'
    test_obj = MostOften(['One', 'One', 1])
    assert test_obj.get_most_often() == 'One'
    test_obj = MostOften(['One', 'One', 1, 2, 2])
    assert test_obj.get_most_often() == 'no clear winner'

    # assert test_obj.unique_items == [1, 7, 8, 2, 3, 5]