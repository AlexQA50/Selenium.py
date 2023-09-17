import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

login = "standard_user"
password = "secret_sauce"

# find username field and send login
user_name = browser.find_element(By.ID, "user-name")
user_name.send_keys(login)

# find password field and send password
password_field = browser.find_element(By.ID, "password")
password_field.send_keys(password)
time.sleep(2)

# find button Login and click
login = browser.find_element(By.ID, "login-button")
login.click()
time.sleep(2)

# find text Products and print in terminal
text_products = browser.find_element(By.CLASS_NAME, "title")
value_text_products = text_products.text
print(value_text_products)

while True:
    pass
