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
    job_name = input('Please input the job name: ')
    job_location = input('Please provide location: ')

    chrome_options = webdriver.ChromeOptions()
    #prevent window from closing
    global driver
    driver = webdriver.Chrome(executable_path=r"D:\Programming\drivers\chromedriver.exe", chrome_options=chrome_options)
    chrome_options.add_argument("--incognito")
    driver.get('https://www.google.com/')
    driver.maximize_window()
    
    #google search field
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    element.clear()
    element.send_keys('LinkedIn: Jobs')
    element.send_keys(Keys.ENTER)

    #find the linkedin search page
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Search for the Right Jobs'))
    )
    element.click()

    #search for the job
    #job_input
    element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input')))
    element.clear()
    element.send_keys(job_name)

    #location
    element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input')))
    element.clear()
    element.send_keys(job_location)
    element.send_keys(Keys.ENTER)

login_linkedin()

