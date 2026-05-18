from selenium.webdriver.common.by import By
from GPT_LEARNING.Phase_8_1_Page_Factory.pages.base_page import BasePage

class DashboardPage(BasePage):

    @property
    def profile_label(self):
        return self.wait_for_visible((By.ID, "profile"))

    @property
    def logout_btn(self):
        return self.wait_for_clickable((By.ID, "logout"))

    def is_logged_in(self):
        return self.profile_label.is_displayed()

    def logout(self):
        self.logout_btn.click()