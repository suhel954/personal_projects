from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#keeping browser option
options = webdriver.ChromeOptions()
options.add_argument('--incognito')

#removing the depreciation error
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.facebook.com/login/')
driver.maximize_window()

'''
CSS Selectors


tag and id combo css selector
syntax: tagname#id input#email
driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('test')

tag and class combo
syntax tagname.class
driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('test') #space is there, sometime it may not consider
driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('test')

tag and attribute combo, tag is optional
syntax tagname[attribut=value]
driver.find_element(By.CSS_SELECTOR, 'input[name=email]').send_keys('test')

tag, class and attribute combo
syntax tagname.class[attribute=value]
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[name=email]').send_keys('test')

'''



# sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
# print(len(sliders))

# links=driver.find_elements(By.TAG_NAME, 'a')
# print(len(links))

# driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')

#link text only for when there is 'a' tagname with href
# driver.find_element(By.LINK_TEXT, 'Register').click()




    
time.sleep(5)