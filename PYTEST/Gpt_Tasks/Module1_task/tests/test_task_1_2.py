import pytest
from Module1_task.myapp.task_1_2 import divide, subtract

def test_subtract():
    assert  subtract(21, 12) == 9
    assert subtract(2, 2) == 0
    assert subtract(-2, -2) == 0
    assert subtract(2, -2) == 4
    assert subtract(2000 , 3230) == -1230

def test_divide():
    assert divide(2, 2) == 1

def test_divide_byZero():
    with pytest.raises(ValueError) as exc:
        divide(2, 0)
    assert str(exc.value) == "Division by zero is not allowed"



