"""class PizzaBuilder:
    def __init__(self):
        self.size = "Regular"
        self.cheese = False
        self.topping = []

    def add_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_topping(self, topping):
        self.topping.extend(topping)
        return self

    def build(self):
        print("Your pizza is build")
        return {
            "size": self.size,
            "cheese": self.cheese,
            "toppings": self.topping
        }

pizza = PizzaBuilder()\
            .add_size("Large")\
            .add_cheese()\
            .add_topping(["Mushroom", "Olives"])\
            .build()

print(pizza)"""

import requests


class APIRequestBuilder:

    def __init__(self):
        self.url = None
        self.method = "GET"
        self.headers = {}
        self.params = {}
        self.payload = None
        self.cookies = {}

    def set_url(self, url):
        self.url = url
        return self

    def set_method(self, method):
        self.method = method.upper()
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def add_param(self, key, value):
        self.params[key] = value
        return self

    def set_json(self, payload):
        self.payload = payload
        return self

    def add_cookie(self, key, value):
        self.cookies[key] = value
        return self


    def send(self):
        response = requests.request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            params=self.params,
            json=self.payload,
            cookies=self.cookies
        )
        return response

builder = APIRequestBuilder()
response = (builder
            .set_url("https://httpbin.org/post")
            .set_method("POST")
            .add_header("Authorization", "Bearer token123")
            .add_header("Content-Type", "application/json")
            .add_param("version", "1.0")
            .set_json({
                "name": "Pranav",
                "role": "QA"
            })
            .add_cookie("session_id", "abc123")
            .send()
)

print(response.status_code)
print(response.json())