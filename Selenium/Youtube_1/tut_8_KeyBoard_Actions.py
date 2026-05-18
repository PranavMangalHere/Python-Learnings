from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")

driver.maximize_window()
input1 = driver.find_element(By.ID, "inputText1")
input2 = driver.find_element(By.ID, "inputText2")

input1.send_keys("heloo Good morning")

actions = ActionChains(driver)

actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

actions.send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").perform()

time.sleep(5)