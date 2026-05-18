"""🟢 1. DemoQA Select Menu
👉 URL: https://demoqa.com/select-menu
🎯 Why it's good:
Has standard dropdown
Has custom dropdown
Has multi-select

🛠 Practice Tasks:
Select using:
visible text
value
Handle multi-select dropdown
Print all options
Validate selected values"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

time.sleep(2)

# Correct locator for standard dropdown
dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))

# Select options
dropdown.select_by_visible_text("Purple")
# dropdown.select_by_value("3")
# dropdown.select_by_index(2)

# Print all options
for option in dropdown.options:
    print(option.text)

time.sleep(2)
driver.quit()

## step 3