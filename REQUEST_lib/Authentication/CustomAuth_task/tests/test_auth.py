import pytest
from Authentication.CustomAuth_task.utils.auth import BearerTokenAuth, BasicAuthClient
from Authentication.CustomAuth_task.utils.api_client import APIClient

BASE_URL = "https://httpbin.org"

@pytest.mark.parametrize("username, password, expected", [
    ("user", "pass", 200),
    ("user", "wrong", 401),
])
def test_basic_auth(username, password, expected):
    auth_client = BasicAuthClient(username, password)
    client = APIClient(BASE_URL, auth=auth_client.get_auth())

    response = client.get("/basic-auth/user/pass")

    assert response.status_code == expected

@pytest.mark.parametrize("token, expected_status", [
    ("valid_token", 200),
    ("", 401),
])
def test_bearer_auth(token, expected_status):

    auth = BearerTokenAuth(token)
    client = APIClient(BASE_URL, auth=auth)

    response = client.get("/bearer")

    assert response.status_code == expected_status

    if expected_status == 200:
        assert response.json()["authenticated"] is True