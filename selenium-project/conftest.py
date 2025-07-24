import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture()
def setup_teardown():
    # setup
    global driver
    options = Options()
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.implicitly_wait(5)
    driver.maximize_window()

    # run test
    yield

    # teardown
    driver.quit()
