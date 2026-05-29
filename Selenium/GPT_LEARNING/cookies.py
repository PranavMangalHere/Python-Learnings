from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core.config import wdm_progress_bar

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

#GETTING ALL COOKIES
cookie=driver.get_cookies()
print(len(cookie))

for c in cookie:
    #GETTING THE DATA OF THE COOKIES
    print(c.get('name'))

#ADDING COOKIES
driver.add_cookie({"name":"sal","value":'10210'})
cookie=driver.get_cookies()
print(len(cookie))

#DELETING COOKIES

driver.delete_cookie('sal')
cookie=driver.get_cookies()
print(len(cookie))

 