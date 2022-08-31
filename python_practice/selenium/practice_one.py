from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

#keeping browser option
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
global driver

#removing the depreciation error
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)

element = driver.find_element(By.NAME, 'username')
element.send_keys('Admin')

element = driver.find_element(By.NAME, 'password')
element.send_keys('admin123')

element = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
element.click()

time.sleep(5)

actual_title = driver.title

expected_title= 'OrangeHRM'

if actual_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

