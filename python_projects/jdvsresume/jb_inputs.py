from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login_linkedin():
    linkedin_username = input('Please provide linkedin username: ')
    linkedin_password = input('Please provide linkedin password: ')
    chrome_options = webdriver.ChromeOptions()
    #prevent window from closing
    global driver
    driver = webdriver.Chrome(executable_path=r"D:\Programming\drivers\chromedriver.exe", chrome_options=chrome_options)
    chrome_options.add_argument("--incognito")
    driver.get('https://www.linkedin.com/')
    driver.maximize_window()
    
    #username field
    element = driver.find_element(By.ID, 'session_key')
    element.clear()
    element.send_keys(linkedin_username)

    #password field
    element = driver.find_element(By.ID, 'session_password')
    element.clear()
    element.send_keys(linkedin_password)

    #login button
    element = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
    element.click()

login_linkedin()

