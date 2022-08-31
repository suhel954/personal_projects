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
driver.get('https://www.google.com')
driver.maximize_window()
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
print(element.is_displayed())
print(element.is_enabled())


element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
if element.is_selected() == True: #status of this element, can be used in an if command
    pass
else:
    element.click()
    element.clear()
    element.send_keys('Boogie',Keys.ENTER)