import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PagamentoInformacoes(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.botao_pagamento = (By.XPATH, "//*[@class='btn_action checkout_button']")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.botao_finalizar_pagamento = (By.XPATH, "//*[@class='btn_primary cart_button']")

    def clicar_botao_pagamento(self):
        self.clicar(self.botao_pagamento)

    def preencher_informacoes(self, first_name, last_name, postal_code):
        self.escrever(self.first_name, first_name)
        self.escrever(self.last_name, last_name)
        self.escrever(self.postal_code, postal_code)
        self.clicar(self.botao_finalizar_pagamento)




