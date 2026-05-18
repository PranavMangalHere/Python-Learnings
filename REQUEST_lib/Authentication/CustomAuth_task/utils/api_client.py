import requests

class APIClient:
    def __init__(self, base_url, auth=None):
        self.base_url = base_url
        self.auth = auth
        self.session = requests.Session()

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = self.session.get(url, auth=self.auth)
        return response