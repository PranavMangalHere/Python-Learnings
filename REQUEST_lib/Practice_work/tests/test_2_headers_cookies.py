import requests

def send_headers(headers):
    response = requests.get("https://httpbin.org/headers", headers=headers)
    data = response.json()
    server_headers = data['headers']
    for k, v in server_headers.items():
        print(f"{k} : {v}")
    assert response.status_code == 200
    assert server_headers["User-Agent"] == headers["User-Agent"]

custom_headers = {
    "User-Agent": "Pranav-API-Tester/1.0",
    "Authorization": "Bearer sample_token_123"
}
# send_headers(custom_headers)

def test_send_task():
    session = requests.Session()
    session.get("https://httpbin.org/cookies/set/session_id/abc123")
    session.get("https://httpbin.org/cookies/set/user/Pranav")
    print(type(session.cookies))
    for k, v in session.cookies.items():
        print(f"{k}, {v}")

BASE_URL = "https://httpbin.org"


"""
Task 9 — Login Session Simulation
Create mini login workflow.
Steps:
Login using Session
Store cookies
Access protected endpoint
Logout
Verify access denied after logout
Concepts
session auth
cookie persistence
state management
"""

def login(session):
    response = session.get(f"{BASE_URL}/cookies/set/session_token/qwe123")
    
    return response

def access_protected_endpoint(session):

    response = session.get(
        f"{BASE_URL}/cookies"
    )
    data = response.json()
    print("\nProtected Endpoint Response:")
    print(data)
    # Validate authenticated session
    assert data["cookies"]["session_token"] == "qwe123"
    print("\nAccess Granted")
    
def logout(session):
    session.cookies.clear()
    
def verify_access_after_logout(session):
    
    response = session.get(f"{BASE_URL}/cookies")
    data = response.json()
    
    assert "session_token" not in data['cookies']

def test_login_workflow():
    session = requests.session()
    
    response = (login(session))
    
    data = response.json()
    
    for k, v in data['cookies'].items():
        print(f"{k} , {v}")
        
    access_protected_endpoint(session)
    
    logout(session)
    
    verify_access_after_logout(session)
    
# test_login_workflow()