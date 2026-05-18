import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
assert "Google" in driver.title
time.sleep(3)
driver.quit()