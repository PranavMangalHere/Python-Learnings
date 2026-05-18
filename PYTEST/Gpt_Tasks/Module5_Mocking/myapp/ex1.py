import requests

database = { 1: "Pranav", 2: "Ayush", 3: "Sahil" }
def get_user_from_db(user_id):
    return database.get(user_id)

def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError