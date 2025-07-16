import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/v1/index.html")

# find_element()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# send_keys
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click
btn_login.click()

# text
product_title = browser.find_element(By.XPATH, "//div[@class='product_label']")
print(product_title.text)
assert product_title.text == "Products"

# get_attribute()
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("class"))
assert img_backpack.get_attribute("class") == "inventory_item_img"
assert not img_backpack.is_displayed()