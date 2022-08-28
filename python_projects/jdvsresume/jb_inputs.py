from time import sleep

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
    wait = WebDriverWait(driver,10)
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
    
    #click on the jobs tab
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="msg-overlay"]/div[1]/header/div[2]')))
    element.click()
    



login_linkedin()

