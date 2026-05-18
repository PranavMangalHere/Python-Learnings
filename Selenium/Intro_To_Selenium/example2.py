from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")

password = driver.find_element(
    By.XPATH,
    "//input[@id='username']/ancestor::div/following-sibling::div//input"
)

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

driver.quit()