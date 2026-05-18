def login(username, password):
    valid_users = {
        "admin": "1234",
        "user":"pass"
    }
    if username not in valid_users:
        return False
    return valid_users[username] == password