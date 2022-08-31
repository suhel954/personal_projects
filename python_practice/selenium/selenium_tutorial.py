from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#keeping browser option
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
global driver

#removing the depreciation error
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://newtours.demoaut.com")
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in")

time.sleep(5)

print(driver.title)

driver.back()

time.sleep(5)

print(driver.title)

driver.forward()

time.sleep(5)

print(driver.title)






