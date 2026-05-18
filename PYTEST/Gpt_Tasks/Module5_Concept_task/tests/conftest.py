import pytest
from Module5_Concept_task.myapp.multi_params_eg import login

@pytest.fixture
def valid_credentials():
    return [
        ("admin", "1234"),
        ("user", "pass"),
    ]

@pytest.fixture
def login_function():
    return login
