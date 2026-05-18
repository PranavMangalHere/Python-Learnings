from requests.auth import AuthBase, HTTPBasicAuth

class BasicAuthClient:
    def __init__(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def get_auth(self):
        return self.auth

class BearerTokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r
