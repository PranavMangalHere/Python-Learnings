from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options= options)

driver.get("https://jqueryui.com/datepicker/")

