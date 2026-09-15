from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        storage_state="auth.json"
    )

    page = context.new_page()

    page.goto("https://www.saucedemo.com/inventory.html")

    print("URL:", page.url)

    print(
        "Products:",
        page.get_by_text("Sauce Labs Backpack").is_visible()
    )

    context.close()
    browser.close()