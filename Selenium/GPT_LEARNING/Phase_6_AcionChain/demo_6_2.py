import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/hovers")

actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

profile = driver.find_element(By.XPATH, "(//img)[1]")

# Hover
actions.move_to_element(profile).perform()

# Wait for text
# username = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "(//h5)[1]"))
# )
#
# print(username.text)

# Click profile
# driver.find_element(By.XPATH, "(//a[text()='View profile'])[1]").click()
time.sleep(2)
driver.quit()