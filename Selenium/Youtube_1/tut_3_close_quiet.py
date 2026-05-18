from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demo.nopcommerce.com")
driver.find_element(By.LINK_TEXT, "Facebook").click()
time.sleep(3)
# driver.close()
driver.quit()