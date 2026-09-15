from playwright.sync_api import expect, Page

def test_home(page: Page):
    # Navigate to TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")

    # Verify page title
    expect(page).to_have_title("React • TodoMVC")

    # Verify Todo input is visible
    todo_input = page.get_by_placeholder("What needs to be done?")
    expect(todo_input).to_be_visible()
