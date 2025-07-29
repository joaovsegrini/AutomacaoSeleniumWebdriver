import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_CT03_login_valido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        # Instacia os objetos
        login_page = LoginPage()
        home_page = HomePage()

        # Realiza login
        login_page.fazer_login("standard_user", "secret_saucezz")

        # Verificar se o login não foi realizado
        login_page.verificar_mensagem_erro_login()

        #Verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagemm_erro_login(mensagem_erro_esperada)
