import pytest
from Basic_operations.get_req import APIClient

@pytest.fixture
def api_client():
    client=APIClient()
    return client
