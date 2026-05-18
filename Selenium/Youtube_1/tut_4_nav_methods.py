from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")
time.sleep(3)
driver.get("https://www.facebook.com")
driver.back()
time.sleep(4)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.close()