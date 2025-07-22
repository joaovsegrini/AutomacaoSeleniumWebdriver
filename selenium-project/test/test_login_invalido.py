from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--guest")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/v1/index.html")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce123")
driver.find_element(By.ID, "login-button").click()
assert driver.find_element(By.XPATH, "//*[@data-test='error']").is_displayed()
