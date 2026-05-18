import pytest

def pytest_collection_modifyitems(config, items):
    print(len(items))
    for item in items:
        if 'api' in item.name:
            item.add_marker(pytest.mark.api)
