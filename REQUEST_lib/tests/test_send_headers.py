import requests

def test_send_headers():
    
    headers = {
        "Company": "OpenAI",
        "Tester": "Pranav",
        "Environment": "QA"
    }
    response = requests.get("https://httpbin.org/headers", headers=headers)
    data = response.json()
    assert data['headers']['Company'] == "OpenAI"
    assert data['headers']['Tester'] == 'Pranav'
    
def test_send_tokens():
    
    token = "hjbjhdsajjhbj"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get("https://httpbin.org/headers", headers=headers)
    
    data = response.json()
    
    assert data['headers']['Authorization'] == "Bearer " + token
    
    
def test_session_cookies():
    s = requests.Session()
    
    login_response = s.post(
    "https://httpbin.org/post",
    data={
        "username": "admin",
        "password": "admin123"
    }
)
    
    print(s.cookies)