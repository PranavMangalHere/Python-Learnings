import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys("Admin")
password.send_keys("admin123")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5)

recurter = driver.find_element(By.XPATH, "//ul[@class = 'oxd-main-menu']//child::li[5]")
recurter.click()
time.sleep(5)