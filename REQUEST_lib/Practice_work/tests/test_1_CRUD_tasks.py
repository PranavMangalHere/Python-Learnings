import requests
import time

url = "https://jsonplaceholder.typicode.com/posts/"

def test_get_req_validation():
    start = time.time()
    response = requests.get(url + '/1')
    end = time.time()
    response_time = end - start
    
    data = response.json()
    print(data)
    print(response_time)
    
    assert response.status_code == 200
    assert response_time < 2
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert data['title'].strip() != ""
    
def test_query_params():
    params = {
        "userId" : 1
    }
    response = requests.get(url , params=params)
    data = response.json()
    print(response.url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    for post in data:
        assert post["userId"] == 1
    
    total = len(data)
    print("total post ", total)


# response = requests.get(url)

# def analyze_header(response):
#     data = response.headers
    
#     print(data["Content-Type"])
#     print(data["Cache-Control"])
#     print(data['Connection'])
#     print("Server :", data.get("Server"))
    
#     mandatory_headers = {
#         "Content-Type",
#         "Cache-Control",
#         "Connection"
#     }
    
#     for header in mandatory_headers:
#         assert header in data,  f"{header} header missing"
    
# analyze_header(response)


def test_post_req():
    payload={
        "userId": 11,
        "title": "qwer", 
        "body": "asdfghjkl poiuytrewq zxcvbnm"
    }
    
    response = requests.post(url , json = payload)
    data = response.json()
    assert response.status_code == 201
    assert data['title'] == payload['title']

def test_put_req():
    payload = {
        "id": 1,
        "title": "new title",
        "body": "new body",
        "userId": 99
    }
    
    response = requests.put(url+'/1', json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "new title"
    assert data["body"] == "new body"
    assert data["userId"] == 99
    print(data)

def test_patch_req():
    payload = {
        "title": "abc title"
    }
    response = requests.patch(url+'/1', json=payload)
    
    data = response.json()
    
    assert response.status_code == 200
    assert data["title"] == "abc title"
    # Remaining fields unchanged
    assert "body" in data
    assert "userId" in data
    print(data)
    

def test_delete_request():

    resource_id = 1

    delete_url = f"{url}/{resource_id}"
    delete_response = requests.delete(delete_url)
    print("DELETE Status Code:", delete_response.status_code)
    assert delete_response.status_code == 200
    get_response = requests.get(delete_url)
    
    if get_response.status_code == 404:
        print("Resource successfully deleted")
    elif get_response.status_code == 200:
        print("Resource still exists")
    else:
        print("Unexpected status code:", get_response.status_code)
        
        

