from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)

driver.quit()


"""
def slow_scroll(driver, step=100, delay=0.2, times=20):
    for _ in range(times):
        driver.execute_script(f"window.scrollBy(0,{step})")
        time.sleep(delay)

# Use it
slow_scroll(driver)
"""
