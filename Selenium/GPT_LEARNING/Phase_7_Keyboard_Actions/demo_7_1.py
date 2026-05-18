import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/text-box/")

username = driver.find_element(By.XPATH, "//input[@id = 'userName']")
username.send_keys("Alice khan")
# username.send_keys(Keys.TAB)
# password = driver.switch_to.active_element
# password.send_keys("test@email.com")
# password.send_keys(Keys.TAB)
#
# driver.switch_to.active_element.send_keys("Address 1")
time.sleep(3)


actions = ActionChains(driver)

actions.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()
username.send_keys(Keys.TAB)

actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(2)
actions.key_down(Keys.CONTROL).send_keys("a").key_down(Keys.BACKSPACE).perform()
time.sleep(3)

