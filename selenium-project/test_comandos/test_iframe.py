import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/frames")

iframe1 = browser.find_element(By.ID, "frame1")
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("iframe1")
time.sleep(2)

iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()
time.sleep(2)
