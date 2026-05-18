def pytest_sessionstart(session):
    print('Start test')

def pytest_sessionfinish(session, exitstatus):
    print('End test')
    print(f"test collected - {session.testscollected}")

