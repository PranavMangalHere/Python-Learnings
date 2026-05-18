from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from Authentication.HTTP_basic_Auth import basic_auth, digest_auth
import pytest
@pytest.mark.parametrize("username, password, expected", [
    ("user", "pass", 200),
    ("user", "Incorrct", 401),
])
def test_basic_auth(username, password, expected):
    auth = HTTPBasicAuth(username, password)
    response = basic_auth(auth)
    assert response.status_code == expected

@pytest.mark.parametrize("username, password, expected", [
    ("user", "pass", 200),
    ("user", "Incorrct", 401),
])
def test_digest_auth(username, password, expected):
    auth = HTTPDigestAuth(username, password)
    response = digest_auth(auth)
    assert response.status_code == expected