from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)
driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(4)

driver.find_element(By.XPATH, "//span[text() = 'Admin']").click()
time.sleep(3)

driver.execute_script("window.scrollBy(0,300)")
time.sleep(3)

rows = len(driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div"))
print(rows)
count = 0
for row in range(1, rows+1):
    status = driver.find_element(By.XPATH, f"//div[@role='table']/div[2]/div[{row}]/div/div[3]/div").text
    # print(status)
    if status == 'Admin':
        count+=1
print("Admin count: ",count)
time.sleep(4)

driver.close()