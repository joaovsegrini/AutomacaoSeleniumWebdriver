import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Add mochila ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        # Verificando add da mochila
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
        assert driver.find_element(By.XPATH,
                                   "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Retornando a shooping
        driver.find_element(By.XPATH, "//*[@class='btn_secondary']").click()

        # Add novo produto
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        # Verificando os 2 produtos no carrinho
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
        assert driver.find_element(By.XPATH,
                                   "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH,
                                   "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
