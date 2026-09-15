"""
Task 9 — Context Isolation ⭐⭐⭐

Create:

Context A
Context B

Set a cookie in Context A.

Then check Context B.

Expected:

Context A → cookie exists
Context B → cookie does NOT exist

This task proves that you understand context isolation.
"""


from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch()

    context_a = browser.new_context()
    context_b = browser.new_context()

    context_a.add_cookies([
        {
            "name": "test_user",
            "value": "Pranav",
            "domain": "example.com",
            "path": "/"
        }
    ])

    cookies_a = context_a.cookies()
    cookies_b = context_b.cookies()

    print("Context A cookies:")
    print(cookies_a)

    print("\nContext B cookies:")
    print(cookies_b)

    context_a.close()
    context_b.close()

    browser.close()