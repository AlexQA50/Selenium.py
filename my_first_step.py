import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

login = "standard_user"
password = "secret_sauce"

user_name = browser.find_element(By.ID, "user-name")
user_name.send_keys(login)

password_field = browser.find_element(By.ID, "password")
password_field.send_keys(password)
time.sleep(2)

login = browser.find_element(By.ID, "login-button")
login.click()
time.sleep(2)

bag = browser.find_element(By.ID, "item_4_title_link")
bag.click()
time.sleep(2)

buy = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
buy.click()
time.sleep(2)

basket = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
basket.click()
time.sleep(2)

checkout = browser.find_element(By.ID, "checkout")
checkout.click()
time.sleep(2)
first_name = browser.find_element(By.ID, "first-name")
first_name.send_keys("Alex")
time.sleep(2)

last_name = browser.find_element(By.ID, "last-name")
last_name.send_keys("Smith")
time.sleep(2)

zip_code = browser.find_element(By.ID, "postal-code")
zip_code.send_keys("00501")
time.sleep(2)

continue_click = browser.find_element(By.ID, "continue")
continue_click.click()
time.sleep(2)

finish = browser.find_element(By.ID, "finish")
finish.click()
time.sleep(2)

back_home = browser.find_element(By.ID, "back-to-products")
back_home.click()

while True:
    pass
