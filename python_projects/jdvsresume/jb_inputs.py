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

    chrome_options = webdriver.ChromeOptions()
    #prevent window from closing
    global driver
    driver = webdriver.Chrome(executable_path=r"D:\Programming\drivers\chromedriver.exe", chrome_options=chrome_options)
    chrome_options.add_argument("--incognito")
    wait = WebDriverWait(driver,20)
    driver.get('https://www.linkedin.com/')
    driver.maximize_window()

    #username
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="session_key"]')))
    element.clear()
    element.send_keys('suhelshaikh607@gmail.com')

    #password
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="session_password"]')))
    element.clear()
    element.send_keys('Gulu@1947')
    element.send_keys(Keys.RETURN)
    
    #move to job links
    driver.get('https://www.linkedin.com/jobs')

    #minimize the message board if it is present
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="msg-overlay-bubble-header__details flex-row align-items-center ml1"]')))
    element.click()

    time.sleep(5)

    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember25"]')))
    element.clear()
    element.send_keys('Test Engineer', Keys.RETURN)



    #switch to current frame
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jobs-search-box-location-id-ember259"]')))
    # element.clear()
    # element.send_keys('Remote')
    # element.send_keys(Keys.RETURN)

    #for job in list, click on each job and copy the JD, try for a single job listing first
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember388"]')))
    print(element.get_attribute('href'))

    #split the JD and create a set

    #grab the API

login_linkedin()

