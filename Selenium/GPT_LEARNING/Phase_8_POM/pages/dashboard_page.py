from selenium.webdriver.common.by import By
from GPT_LEARNING.Phase_8_POM.pages.base_page import BasePage

class DashboardPage(BasePage):

    PROFILE_LABEL = (By.ID, "profile")
    LOGOUT_BTN = (By.ID, "logout")

    def is_logged_in(self):
        return self.find(self.PROFILE_LABEL).is_displayed()

    def logout(self):
        self.click(self.LOGOUT_BTN)

