import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/context_menu")

actions = ActionChains(driver)

box = driver.find_element(By.ID, "hot-spot")

# Right click
actions.context_click(box).perform()
time.sleep(2)

alert = driver.switch_to.alert
alert.accept()
time.sleep(2)