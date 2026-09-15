import time
from playwright.sync_api import Page, expect

""" 
get_by_alt_text
get_by_text
get_by_Role
get_by_label
get_by_placeholder
get_by_title
get_by_test_id (data-test_id)

"""

def test_verify_pwlocators(page: Page):
    page.goto("https://www.qa-practice.com/")
    expect(page).to_have_url("https://www.qa-practice.com/")
    # time.sleep(5)
    expect(page).to_have_title("Home Page | QA Practice")
    text = page.get_by_text("Hello!")
    expect(text).to_be_visible()

    # getByRole
    page.goto("https://www.qa-practice.com/forms/practice-form")
    expect(page.get_by_role("heading", name = "Student Registration Form")).to_be_visible()

    #get_by_label
    page.get_by_label('First Name*').fill("Pranav")
    page.get_by_label("Last Name*").fill("Mangal")
    page.wait_for_timeout(2000)

    # page.get_by_title()
