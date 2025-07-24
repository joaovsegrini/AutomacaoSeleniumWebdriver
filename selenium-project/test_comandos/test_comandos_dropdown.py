# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(12)
#
# browser.maximize_window()
# browser.get("https://chercher.tech/practice/dropdown-selenium-webdriver")
#
# dropdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
# dropdown_products.select_by_visible_text("Google")
# time.sleep(2)
#
# dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
# dropdown_animals.select_by_value("babycat")
# time.sleep(2)
# dropdown_animals.select_by_index(3)
# time.sleep(2)
#
# dropdown_food = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
# dropdown_food.select_by_visible_text("Pizza")
# time.sleep(2)
# dropdown_food.select_by_visible_text("Bonda")
# time.sleep(2)