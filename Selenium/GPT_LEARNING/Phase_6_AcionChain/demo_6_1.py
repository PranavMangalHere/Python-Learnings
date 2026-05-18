import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

button = driver.find_element(By.XPATH, "//button[text() = 'Add Element']")

button.click()
time.sleep(2)

actions = ActionChains(driver)

actions.click(button)
time.sleep(2)

actions.click(button).perform()
time.sleep(2)