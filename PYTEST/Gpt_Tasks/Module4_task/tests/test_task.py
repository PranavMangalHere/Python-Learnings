from Module4_task.myapp.task import login
import pytest

users = [
("admin", "Yes you can login"),
    ("guest", "No"),
    ("editor", "No"),
    ("invalid_user", "No"),
    ("locked_user", "No"),
]

@pytest.fixture(params=users)
def login_data(request):
    username, expected = request.param
    result = login(username)
    return result, expected

def test_login(login_data):
    result, expected = login_data
    assert result == expected
