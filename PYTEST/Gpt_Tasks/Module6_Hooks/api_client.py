import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get_req(self, endpoint):
        headers = {"content-type": "application/json"}
        final_url = self.base_url + endpoint
        response = requests.get(final_url, headers=headers)
        return response

    def post_req(self, endpoint, payload):
        headers = {"content-type": "application/json"}
        final_url = self.base_url + endpoint
        response = requests.post(final_url, json=payload, headers=headers)
        return response

    def put_req(self, endpoint, payload):
        headers = {"content-type": "application/json"}
        final_url = self.base_url + endpoint
        response = requests.put(final_url, json=payload, headers=headers)
        return response

    def delete_req(self, endpoint):
        headers = {"content-type": "application/json"}
        final_url = self.base_url + endpoint
        response = requests.delete(final_url, headers=headers)
        return response