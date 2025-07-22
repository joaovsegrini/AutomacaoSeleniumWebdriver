from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--guest")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/v1/index.html")
driver.implicitly_wait(5)
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add mochila ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

# Verificando add da mochila
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# Finalizando compra
driver.find_element(By.XPATH, "//*[@class='btn_action checkout_button']").click()
driver.find_element(By.ID, "first-name").send_keys("Matheus")
driver.find_element(By.ID, "last-name").send_keys("Silva")
driver.find_element(By.ID, "postal-code").send_keys("120007145")
driver.find_element(By.XPATH, "//*[@class='btn_primary cart_button']").click()
driver.find_element(By.XPATH, "//*[@class='btn_action cart_button']").click()
assert driver.find_element(By.XPATH, "//*[@class='complete-header' and text()='THANK YOU FOR YOUR ORDER']").is_displayed()




