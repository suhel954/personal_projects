#this can be used to get all the links in the linkedin page
'''
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

for link in links:
    print(link.get_attribute('href'))

'''




from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login_linkedin():

    #Inputs

    # linkedin_username = input('Please provide linkedin username: ')
    # linkedin_password = input('Please provide linkedin password: ')
    # job_name = input('Please input the job name: ')
    # job_location = input('Please provide location: ')

    pass

login_linkedin()

