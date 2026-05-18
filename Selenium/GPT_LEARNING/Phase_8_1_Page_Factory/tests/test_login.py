from GPT_LEARNING.Phase_8_1_Page_Factory.pages.login_page import LoginPage
from GPT_LEARNING.Phase_8_1_Page_Factory.utils.config import BASE_URL
from GPT_LEARNING.Phase_8_1_Page_Factory.utils.test_data import VALID_USER, INVALID_USER


def test_valid_login(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    dashboard = login.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    assert dashboard.is_logged_in()


def test_invalid_login(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login(
        INVALID_USER["username"],
        INVALID_USER["password"]
    )

    assert "Invalid" in login.get_error_message()