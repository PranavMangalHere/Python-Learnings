from selenium.webdriver.common.by import By

class LoginAdminPage:
    USERNAME_ID = 'Email'
    PASSWORD_ID = 'Password'
    btn_login_xpath = "//button[@type = 'submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.USERNAME_ID).clear()
        self.driver.find_element(By.ID, self.USERNAME_ID).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.PASSWORD_ID).clear()
        self.driver.find_element(By.ID, self.PASSWORD_ID).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    