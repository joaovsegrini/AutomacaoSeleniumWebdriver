import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FinalizarCompra(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.clica_botao_finalizar = (By.XPATH, "//*[@class='btn_action cart_button']")
        self.mensagem_compra_finalizada = (By.XPATH, "//*[@class='complete-header' and text()='THANK YOU FOR YOUR ORDER']")

    def verificar_produto_final(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def botao_finalizando_compra(self):
        self.clicar(self.clica_botao_finalizar)

    def compra_finalizada(self):
        self.verificar_se_elemento_existe(self.mensagem_compra_finalizada)


