from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
print(driver)
print(driver.get("https://www.google.com"))
print(driver.title)
print(driver.current_url)
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Who is Dhoni")
# search_box.submit()