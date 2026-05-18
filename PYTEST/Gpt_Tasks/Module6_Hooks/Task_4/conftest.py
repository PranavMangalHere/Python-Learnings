def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if call.excinfo is None:
            print('PASSED..)')
        else:
            print('FAILED..)')