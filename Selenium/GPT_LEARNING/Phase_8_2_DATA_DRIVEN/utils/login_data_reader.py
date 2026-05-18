import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(BASE_DIR, "../test_data/login_data.json")

def get_json_login_data():
    with open(file, "r") as f:
        data = json.load(f)
    return [ (i["username"], i["password"], i["expected"]) for i in data ]

print(get_json_login_data())
