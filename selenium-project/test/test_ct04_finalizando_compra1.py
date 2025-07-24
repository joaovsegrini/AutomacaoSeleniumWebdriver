import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.finalizando
class TestCT04:
    def test_ct04_finalizar_compra1(self):
        driver = conftest.driver
        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Adicionando mochila ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

        # Verificando adição da mochila
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link fa-layers fa-fw']").click()
        assert driver.find_element(By.XPATH,
                                   "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Finalizando compra
        driver.find_element(By.XPATH, "//*[@class='btn_action checkout_button']").click()
        driver.find_element(By.ID, "first-name").send_keys("Matheus")
        driver.find_element(By.ID, "last-name").send_keys("Silva")
        driver.find_element(By.ID, "postal-code").send_keys("120007145")
        driver.find_element(By.XPATH, "//*[@class='btn_primary cart_button']").click()
        driver.find_element(By.XPATH, "//*[@class='btn_action cart_button']").click()
        assert driver.find_element(By.XPATH,
                                   "//*[@class='complete-header' and text()='THANK YOU FOR YOUR ORDER']").is_displayed()
