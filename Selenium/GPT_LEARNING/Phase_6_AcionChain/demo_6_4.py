from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

actions = ActionChains(driver)

actions.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(4)

