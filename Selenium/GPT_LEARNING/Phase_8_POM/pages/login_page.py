from selenium.webdriver.common.by import By
from GPT_LEARNING.Phase_8_POM.pages.base_page import BasePage
from GPT_LEARNING.Phase_8_POM.pages.dashboard_page import DashboardPage

class LoginPage(BasePage):

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")
    ERROR_MSG = (By.ID, "error")

    # Actions
    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return DashboardPage(self.driver)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)