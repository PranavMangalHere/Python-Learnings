import csv
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR,"test_data", "login_csv_data.csv")

def read_csv(file_path):
    with open(file_path, newline="") as csvfile:
        data = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        return data

def get_login_csv_data():
    data = read_csv(file_path)

    return [
        (i["username"], i["password"], i["expected"]) for i in data
    ]

print(get_login_csv_data())
