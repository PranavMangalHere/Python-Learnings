import pytest
from Module6_Hooks.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

def pytest_collection_modifyitems(config, items):
    for item in items:

        # Option 1: If test uses api_client fixture
        if "api_client" in item.fixturenames:
            item.add_marker(pytest.mark.api)

        # Option 2: If test name contains "api"
        elif "api" in item.name.lower():
            item.add_marker(pytest.mark.api)

