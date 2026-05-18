from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()

# driver.get("http://www.deadlinkcity.com/")
#
# all_links = driver.find_elements(By.TAG_NAME, 'a')
# broken_link_count = 0
# good_link_count = 0
# for link in all_links:
#     url = link.get_attribute('href')
#     try:
#         response = requests.head(url)
#     except:
#         None
#
#     if response.status_code >= 400:
#         print("broken link: ", url)
#         broken_link_count += 1
#     else:
#         print("good link: ", url)
#         good_link_count += 1
#
# print("broken link count:  --->",broken_link_count)
# print("good link count  :  --->",good_link_count)

driver.get("https://testautomationpractice.blogspot.com/")

elms = driver.find_elements(By.XPATH, "//table[@name= 'BookTable']//tr/td[4]")
lst = []
for ele in elms:
    lst.append(int(ele.text))
print(lst)
print(max(lst))
