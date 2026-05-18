import requests

# def get_post(post_id):
#     response = requests.get( f"https://jsonplaceholder.typicode.com/posts/{post_id}" )
#     response.raise_for_status()
#     return response.json()

# def get_users():
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
#     # print(response)
#     return response
#
# get_users()

BASE_URL = "http://jsonplaceholder.typicode.com/"


class APIClient:
    def __init__(self):
        self.BASE_URL = BASE_URL


    def get_req(self,endpoint):
        response = requests.get(self.BASE_URL + endpoint)

        return response

    def get_specific_user(self, endpoint):
        response = requests.get(self.BASE_URL + endpoint)

        return response

    def post_req(self,endpoint):
        payload = {
            "name":"Sahil",
            "email":"abc@example.com"
        }
        response = requests.post(self.BASE_URL + endpoint,
                                 params=payload)

        return response

    def put_req(self, endpoint):
        payload = {
            "name":"Sahil"
        }
        response = requests.put(self.BASE_URL + endpoint,params=payload)
        return response

    def del_req(self, endpoint):
        payload = {
            "name":"Sahil"
        }
        response = requests.delete(self.BASE_URL + endpoint,params=payload)
        return response

