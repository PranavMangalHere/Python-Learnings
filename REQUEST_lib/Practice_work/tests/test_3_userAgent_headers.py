""" 
Task 10 — User-Agent Spoofing
Tasks:
Send Chrome User-Agent
Send Firefox User-Agent
Send Bot User-Agent
Compare responses
Concepts
User-Agent
browser simulation
"""

import requests
url = "https://httpbin.org/user-agent"
def send_user_agent(user_agent_name, user_agent_value):

    headers = {
        "User-Agent": user_agent_value
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(f"\n{user_agent_name} Request")
    print("-" * 40)
    print("Sent User-Agent:")
    print(user_agent_value)
    print("\nServer Received:")
    print(data["user-agent"])
    # Validation
    assert data["user-agent"] == user_agent_value
    print("\nValidation Successful")
# --------------------------------
# Chrome User-Agent
# --------------------------------
chrome_ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)
send_user_agent("Chrome", chrome_ua)
# --------------------------------
# Firefox User-Agent
# --------------------------------
firefox_ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) "
    "Gecko/20100101 Firefox/125.0"
)
send_user_agent("Firefox", firefox_ua)
# --------------------------------
# Bot User-Agent
# --------------------------------
bot_ua = "MyCustomBot/1.0"
send_user_agent("Bot", bot_ua)