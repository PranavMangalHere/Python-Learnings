# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:

#     browser = p.chromium.launch()

#     context = browser.new_context(
#         viewport={'width':1920, 'height':1080},
#         locale='em-IN',
#         timezone_id="Asia/Kolkata",
#         color_scheme="dark",
#         permissions=["geolocation"],
#         geolocation={
#             "latitude": 17.3850,
#             "longitude": 78.4867
#         }
#     )
#     page = context.new_page()
#     page.goto("https://example.com")
#     print(page.title())
#     context.close()
#     browser.close()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch()

    admin_context = browser.new_context()
    user_context = browser.new_context()

    admin_page = admin_context.new_page()
    user_page = user_context.new_page()

    admin_page.goto("https://example.com")
    user_page.goto("https://example.com")

    admin_context.close()
    user_context.close()

    browser.close()