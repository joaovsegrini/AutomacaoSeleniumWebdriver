import pytest
from pages.carrinho_page import CarrinhoPage
from pages.finalizar_compra_page import FinalizarCompra
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pagamento_informacoes import PagamentoInformacoes


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.finalizando
class TestCT05:
    def test_ct05_finalizando_compra2(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        pagamento_informacoes = PagamentoInformacoes()
        finalizando_compra = FinalizarCompra()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"

        # Realiza login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Add produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando produto
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Retornando a shooping
        carrinho_page.clicar_continuar_comprando()

        # Adicionando novo produto
        home_page.adicionar_ao_carrinho(produto_2)

        # Verificando os 2 produtos no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

        # Pagamento da compra
        pagamento_informacoes.clicar_botao_pagamento()
        pagamento_informacoes.preencher_informacoes("Matheus", "Silva", "1234567")

        #Finalizando a compra
        finalizando_compra.verificar_produto_final(produto_1)
        finalizando_compra.verificar_produto_final(produto_2)
        finalizando_compra.botao_finalizando_compra()
        finalizando_compra.compra_finalizada()
