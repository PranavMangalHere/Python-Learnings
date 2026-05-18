def pytest_runtest_call(item):
    print(f"{item.nodeid}, {item.location}, {item.name}")