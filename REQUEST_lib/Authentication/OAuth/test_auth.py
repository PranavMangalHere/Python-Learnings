import requests
import pytest

access_token = None

# 1113546419273-joj7am4554t5oe8201blsdtei63r5joo.apps.googleusercontent.com
# DOCSPX-CoTypFEpI_lcCRLj1iZIVvQhvW-1

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8080/callback"

# 🔥 Paste fresh code from browser every time
AUTH_CODE = "PASTE_YOUR_AUTH_CODE_HERE"
def get_access_token():
    url = "https://oauth2.googleapis.com/token"

    data = {
        "code": AUTH_CODE,  # ✅ REQUIRED
        "client_id": "1013546419273-joj7am4554t5oe8201blsdtei63r5joo.apps.googleusercontent.com",
        "client_secret": "DOCSPX-CoTypFEpI_lcCRLj1iZIVvQhvW-1",
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    res = requests.post(url, data=data)

    # 🔍 Debug (VERY IMPORTANT)
    print("STATUS:", res.status_code)
    print("RESPONSE:", res.text)

    if res.status_code != 200:
        raise Exception(f"Token generation failed: {res.text}")

    return res.json()["access_token"]


def test_google_userinfo():
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers=headers
    )

    print("USER INFO:", res.text)

    assert res.status_code == 200
    assert "name" in res.json()