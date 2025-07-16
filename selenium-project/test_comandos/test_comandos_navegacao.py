import time
from selenium import webdriver

browser = webdriver.Chrome()

# maximize_window()
browser.maximize_window()
browser.minimize_window()

# get()
browser.get("https://google.com")

# refresh()
browser.refresh()

# get()
browser.get("https://www.saucedemo.com/v1/index.html")
time.sleep(2)

# back()
browser.back()
time.sleep(2)

# forward()
browser.forward()
time.sleep(2)

# browser.switch_to.new_window("tab")
# time.sleep(2)
#
# # close()
# browser.close()
# time.sleep(2)

browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(2)

# quit()
browser.quit()


