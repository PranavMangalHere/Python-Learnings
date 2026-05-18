from selenium.webdriver.common.by import By
from GPT_LEARNING.Phase_8_1_Page_Factory.pages.base_page import BasePage
from GPT_LEARNING.Phase_8_1_Page_Factory.pages.dashboard_page import DashboardPage



class LoginPage(BasePage):

    @property
    def username(self):
        return self.wait_for_visible((By.ID, "username"))

    @property
    def password(self):
        return self.wait_for_visible((By.ID, "password"))

    @property
    def login_btn(self):
        return self.wait_for_clickable((By.ID, "loginBtn"))

    @property
    def error_msg(self):
        return self.wait_for_visible((By.ID, "error"))

    # Actions
    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_btn.click()

        return DashboardPage(self.driver)

    def get_error_message(self):
        return self.error_msg.text