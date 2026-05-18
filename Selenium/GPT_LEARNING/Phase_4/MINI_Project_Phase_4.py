from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)
## name and email
f_name = driver.find_element(By.ID, "firstName")
l_name = driver.find_element(By.ID, "lastName")
email = driver.find_element(By.ID, "userEmail")

f_name.send_keys("Pranav")
l_name.send_keys("Tester")
email.send_keys("test@email.com")

# gender checkbox
radio = driver.find_elements(By.XPATH, "//label[contains(@for,'gender-radio')]")

for check in radio:
    if check.text == 'Male':
        check.click()
time.sleep(2)

## step 3
checkboxes = driver.find_elements(By.XPATH, "//label[contains(@for,'hobbies-checkbox')]")
for checkbox in checkboxes:
    if checkbox.text in ['Sports', 'Reading']:
        checkbox.click()

if driver.find_element(By.ID, "hobbies-checkbox-2").is_selected():
    driver.find_element(By.ID, "hobbies-checkbox-2").click()

time.sleep(2)

## step 4

upload = driver.find_element(By.ID, "uploadPicture")

upload.send_keys("C:\\Users\PranavMangal\Desktop\Python my work deep dive\Selenium\GPT_LEARNING\Phase_4\\abc.txt")

time.sleep(2)

## step 5 - validation

assert f_name.get_attribute("value") == "Pranav"
assert l_name.get_attribute("value") == "Tester"
assert email.get_attribute("value") == "test@email.com"

assert driver.find_element(By.ID, "gender-radio-1").is_selected()

assert driver.find_element(By.ID, "hobbies-checkbox-1").is_selected()
assert driver.find_element(By.ID, "hobbies-checkbox-2").is_selected() == False