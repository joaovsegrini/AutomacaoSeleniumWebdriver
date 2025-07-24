import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_CT03_login_valido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce111")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//*[@data-test='error']").is_displayed()
