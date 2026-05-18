from selenium.webdriver.common.by import By
from POM_Design.Example_1.pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LoginButton = (By.CLASS_NAME, "radius")

    def login(self, username, password):
        self.type(self.USERNAME, self.USERNAME)
        self.type(self.PASSWORD, self.PASSWORD)
        self.click(self.LoginButton)
