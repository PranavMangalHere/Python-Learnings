import pytest
from Youtube_Tutorial.tut4.myapp.sample import add

# def test_add_num():
#     assert add(1, 2) == 3
#
# def test_add_str():
#     assert add("hello", "world") == "helloworld"
#
# def test_add_list():
#     assert add([1], [2]) == [1,2]
    # raise Exception()

@pytest.mark.parametrize('a,b, c', [
    (1, 2, 3),
    ('a', 'b', 'ab'),
    ([1,2], [21,32], [1,2,21,32])
], ids=['int', 'str', 'list'])
def test_add(a,b, c):
    assert add(a, b) == c