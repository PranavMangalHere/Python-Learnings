import pytest
@pytest.fixture
def api_client():
    print("Creating API client")
    client = {"base_url": "https://api.example.com"}
    yield client
    print("Closing API client")

def pytest_runtest_call(item):
    if "api_client" in item.fixturenames:
        print("Api Test")