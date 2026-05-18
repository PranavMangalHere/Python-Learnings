from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(5)

checkbox_gender = driver.find_element(By.XPATH, "//input[@value='Male']").click()

assert driver.find_element(By.ID, "gender-radio-1").is_selected()
time.sleep(2)

driver.find_element(By.XPATH, "//label[text()='Sports']").click()
read = driver.find_element(By.XPATH, "//label[text()='Reading']")

read.click()

time.sleep(2)

read.click()

time.sleep(2)
assert driver.find_element(By.ID, "hobbies-checkbox-1").is_selected() == True
