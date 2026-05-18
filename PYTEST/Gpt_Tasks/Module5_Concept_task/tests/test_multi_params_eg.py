# from Module5_Concept_task.myapp.multi_params_eg import login
import pytest

"""# Multiple Parameters Example
@pytest.mark.parametrize("username, password, expected",[
    ("admin", "1234",True),
    ("user", "pass", True),
    ("admin", "wrong", False),
    ("invalid", "1234", False),
])
def test_login(username, password, expected):
    result = login(username, password)
    assert result == expected"""

# edge Cases Example
"""@pytest.mark.parametrize("username,password,expected", [
    ("", "", False),             # empty
    ("admin", "", False),        # empty password
    ("", "1234", False),         # empty username
    (None, None, False),         # None values
    ("ADMIN", "1234", False),    # case sensitive
])

def test_login_edge_cases(username, password, expected):
    result = login(username, password)
    assert result == expected"""


import pytest

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "1234", True),
        ("user", "pass", True),
        ("admin", "wrong", False),
        ("invalid", "1234", False),
    ]
)
def test_login(login_function, username, password, expected):
    result = login_function(username, password)
    assert result == expected
