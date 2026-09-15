from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    # Navigate
    page.goto("https://example.com")

    print("Current URL:", page.url)

    # Navigate somewhere else
    page.goto("https://example.org")

    print("Current URL:", page.url)

    # Go back
    page.go_back()

    print("After back:", page.url)

    # Go forward
    page.go_forward()

    print("After forward:", page.url)

    # Reload
    page.reload()

    print("After reload:", page.url)

    browser.close()