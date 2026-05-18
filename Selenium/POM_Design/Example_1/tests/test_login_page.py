from selenium import webdriver
from POM_Design.Example_1.pages.login_page import LoginPage

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)

    login_page.login("tomsmith", "SuperSecretPassword!")

    driver.quit()