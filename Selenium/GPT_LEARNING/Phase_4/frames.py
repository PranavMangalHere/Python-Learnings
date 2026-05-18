from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)

# Switch to iframe
frame = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
driver.switch_to.frame(frame)

# Type inside editor
editor = driver.find_element(By.ID, "tinymce")
editor.clear()
editor.send_keys("Hello Pranav!")

# Switch back
driver.switch_to.default_content()

# Verify outside element
assert driver.find_element(By.TAG_NAME, "h3").is_displayed()