import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

def basic_auth(auth):
    response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=auth)

    return response

def digest_auth(auth):
    response = requests.get("https://httpbin.org/digest-auth/auth/user/pass", auth = auth)

    return response
