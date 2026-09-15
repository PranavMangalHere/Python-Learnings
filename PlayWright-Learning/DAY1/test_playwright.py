from playwright.sync_api import Page, expect

def test_verify(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_verifyTitle(page:Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    mytitle = page.title()
    print(mytitle)
    expect(page).to_have_title("OrangeHRM")


