from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#keeping browser option
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

#removing the depreciation error
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://demo.nopcommerce.com')
driver.maximize_window()

# driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')

#link text only for when there is 'a' tagname with href
# driver.find_element(By.LINK_TEXT, 'Register').click()


    
#time.sleep(5)