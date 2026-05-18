import sys

import pytest
from Youtube_Tutorial.tut3.myapp.sample import add

@pytest.mark.skip(reason = "just wan a skip")
def test_add_num():
    assert add(1, 2) == 3
def test_add_str():
    assert add("hello", "world") == "helloworld"

@pytest.mark.xfail(sys.platform == "linux", reason="fail on linux")
def test_add_list():
    assert add([1], [2]) == [1,2]
    # raise Exception()

class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3
    def test_add_str(self):
        assert add("hello", "world") == "helloworld"



