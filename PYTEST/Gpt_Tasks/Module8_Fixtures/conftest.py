import pytest

@pytest.fixture(scope="session")
def session_fix():
    print("Session start")
    yield
    print("session end")

@pytest.fixture(scope="module")
def module_fix():
    print("module start")
    yield
    print("module end")
    
@pytest.fixture
def func_fix():
    print("func start")
    yield
    print("func end")
