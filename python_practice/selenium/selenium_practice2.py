from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = FirefoxOptions()
options.browser_version = '92'

driver = webdriver.Remote(options=options)


#driver = webdriver.Firefox()
# Go to signup form
timestamp = time.time()

driver.get("https://selenium-blog.herokuapp.com/signup")
# Fill out and submit form
username_field = driver.find_element(By.ID, 'user_username')     #id: )
username_field.send_keys(f"user {timestamp}")

email_field = driver.find_element(By.ID, 'user_email')
email_field.send_keys(f"user{timestamp}@test.com")

password_field = driver.find_element(By.ID, 'user_password')
password_field.send_keys("password")

sign_up_button = driver.find_element(By.ID, 'submit')
sign_up_button.click()

# Confirm user is signed up successfully
assert "Welcome to the alpha blog user" in driver.page_source

driver.quit()