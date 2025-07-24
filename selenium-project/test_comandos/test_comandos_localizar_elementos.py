# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
#
# browser.maximize_window()
# browser.get("https://www.saucedemo.com/v1/index.html")
#
# # find_element()
# # username = browser.find_element(By.ID, "user-name")
# # password = browser.find_element(By.ID, "password")
#
# # send_keys
# # username.send_keys("standard_user")
# # password.send_keys("secret_sauce")
#
# # find_elements()
# auth_fields = browser.find_elements(By.XPATH, "//*[@class='form_input']")
# print(auth_fields)
# print(len(auth_fields))
# assert len(auth_fields) == 2
#
# time.sleep(5)
#
# browser.quit()