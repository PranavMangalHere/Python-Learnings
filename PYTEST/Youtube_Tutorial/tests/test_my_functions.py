import pytest
import Youtube_Tutorial.Source.my_functions as my_functions

def test_divide():
    result = my_functions.divide(12, 2)
    assert result == 6
def  test_add():
    result = my_functions.add(12, 2)
    assert result == 14