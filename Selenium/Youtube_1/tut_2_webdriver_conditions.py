from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.facebook.com/signup")
first_name = driver.find_element(By.XPATH, '//*[@id="_R_1cl2p4jikacppb6amH1_"]')
print(first_name.is_displayed())
print(first_name.is_enabled())