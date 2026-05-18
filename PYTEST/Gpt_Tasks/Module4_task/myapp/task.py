"""✅ TASK 1 — Create User Login Fixture
Goal:
Simulate login
Print setup & teardown
Return user object"""

def login(name):
    if name == "admin":
        return "Yes you can login"
    else:
        return "No"
