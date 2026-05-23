import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://httpbin.org/"

"""
Task 11 — Basic Authentication Tester
Using:
HTTPBin Basic Auth
Tasks:
Test valid credentials
Test invalid credentials
Handle 401 responses
Create reusable auth function
Concepts
Basic Auth
auth=
401 testing
"""

def test_basic_auth():
    
    response = requests.get(f"{BASE_URL}/basic-auth/user/passwd", auth=HTTPBasicAuth("user", "passwd"))
    data = response.json()
    assert response.status_code == 200
    print(data)
    assert data["authenticated"] is True
    print("\nValid Authentication Successful")

# test_basic_auth()


""" 
Task 12 — Bearer Token Framework
Tasks:
Create token manager
Send Bearer token
Validate Authorization header
Test invalid token
Test missing token
Concepts
Bearer Auth
reusable headers
"""

def test_bearer_token_auth():
    token = "qwe123"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(f"{BASE_URL}/headers", headers= headers)
    
    data = response.json()
    assert response.status_code == 200
    print(data['headers']['Authorization'])
    assert data['headers']['Authorization'] == f"Bearer {token}"
    
# test_bearer_token_auth()


""" 
Task 13 — OAuth Client Credentials Flow
Simulate OAuth flow.
Tasks:
Request token
Extract access token
Use token in protected API
Validate expiry field
Test invalid client secret
Concepts
OAuth
token extraction
protected APIs
"""

def request_token(client_id, client_secret):
    
    valid_id = "client_app"
    valid_secret= "123qwe"
    
    if client_id == valid_id and client_secret == valid_secret:
        token_data = {
            "access_token" : "oauth_access_token_abc123",
            "token_type" : "Bearer",
            "expires_in": 3600
        }
        return 200, token_data
    
    else:
        error_response = {
            "error": "invalid_client"
        }
        return 401, error_response

def access_protected_api(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)
    
    return response

def test_valid_cred():
    status_code, token_data = request_token(
        "client_app",
        "123qwe"
    )
    
    assert status_code == 200
    
    access_token = token_data['access_token']
    
    assert token_data["expires_in"] > 0
    response = access_protected_api(access_token)
    
    data = response.json()
    print(data)
    
    assert response.status_code == 200

    assert data["authenticated"] is True

    assert data["token"] == access_token
    
test_valid_cred()
    
def test_invalid_cred():
    pass