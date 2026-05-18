import pytest
from selenium import webdriver
from pages.login_admin_page import LoginAdminPage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Test_01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = 'admin@yourstore.com'
    password = 'admin'
    invalid_username = 'adminrandom@yourstore.com'

    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        if actual_title == expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_login(self):
        option = Options()
        option.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=option)
        self.driver.get(self.admin_page_url)
        self.admin_login_page = LoginAdminPage(self.driver)

        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login()

        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class ='content-header']/h1").text()

        if act_dashboard_text == 'Dashboard':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_invalid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_login_page = LoginAdminPage(self.driver)

        self.admin_login_page.enter_username(self.invalid_username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login()

        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class ='content-header']/h1").text()

        if act_dashboard_text == 'Dashboard':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False