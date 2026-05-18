import pytest
from Youtube_Tutorial.Source.Task_functions import multiply

def test_multiply():
    assert multiply(12, 2) == 24
    assert multiply(12, 0) == 0
    assert multiply(32, 3) == 96
