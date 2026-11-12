"""
Classe Pedido (aula de 12/11).

Fontes para estudar:
- Herança:
  https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance
- Laço for:
  https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements
- raise: como gerar um erro:
  https://docs.python.org/pt-br/3/tutorial/errors.html#raising-exceptions
- f-string (texto com variáveis):
  https://docs.python.org/pt-br/3/tutorial/inputoutput.html#formatted-string-literals
- Livro: GUEDES, G. T. A. UML 2: uma abordagem prática. 3. ed. Novatec, 2018.
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from models.cartao import Cartao
from models.pix import Pix


class Pedido:
    """
    Compra de um cliente.

    AGREGAÇÃO: o pedido recebe os itens que o carrinho já criou.
    POLIMORFISMO: total() chama calcular_total() sem saber se é Pix ou Cartao.
    """

    def __init__(self, numero, cliente, forma_pagamento, parcelas=1):
        if cliente.carrinho.esta_vazio():    # RN6: carrinho vazio não fecha pedido
            raise ValueError("O carrinho está vazio: não dá para fechar o pedido.")

        self.__numero = numero
        self.__cliente = cliente
        self.__itens = cliente.carrinho.itens    # agregação
        self.__status = "aberto"

        # O pedido cria o pagamento a partir da escolha do cliente
        if forma_pagamento == "pix":
            self.__pagamento = Pix(self.subtotal())
        elif forma_pagamento == "cartao":
            self.__pagamento = Cartao(self.subtotal(), parcelas)
        else:
            raise ValueError("Forma de pagamento inválida: use 'pix' ou 'cartao'.")

    @property
    def numero(self):
        return self.__numero

    @property
    def status(self):
        return self.__status

    @property
    def itens(self):
        return list(self.__itens)

    @property
    def pagamento(self):
        return self.__pagamento

    def subtotal(self):
        """Soma dos itens, sem desconto e sem juros."""
        soma = 0.0
        for item in self.__itens:
            soma += item.subtotal()
        return round(soma, 2)

    def total(self):
        """Valor final: quem calcula é o pagamento (polimorfismo)."""
        return self.__pagamento.calcular_total()

    def confirmar(self):
        """RN11: confirmar baixa o estoque. RN7: o carrinho esvazia depois."""
        if self.__status != "aberto":
            raise ValueError(f"O pedido {self.__numero} já está {self.__status}.")

        # Primeiro confere tudo; só depois baixa o estoque
        for item in self.__itens:
            if not item.produto.tem_estoque(item.quantidade):
                raise ValueError(f"Estoque insuficiente de {item.produto.nome}.")
        for item in self.__itens:
            item.produto.baixar_estoque(item.quantidade)

        self.__status = "confirmado"
        self.__cliente.carrinho.limpar()          # RN7
        self.__cliente.adicionar_pedido(self)

    def cancelar(self):
        """RN11: cancelar devolve as unidades ao estoque."""
        if self.__status != "confirmado":
            raise ValueError("Só dá para cancelar um pedido confirmado.")
        for item in self.__itens:
            item.produto.repor_estoque(item.quantidade)
        self.__status = "cancelado"

    def __str__(self):
        linhas = [f"Pedido {self.__numero} ({self.__status}) - {self.__cliente.nome}"]
        for item in self.__itens:
            linhas.append(f"  {item}")
        linhas.append(f"  Subtotal: R$ {self.subtotal():.2f}")
        linhas.append(f"  Pagamento: {self.__pagamento.descricao()}")
        linhas.append(f"  TOTAL: R$ {self.total():.2f}")
        return "\n".join(linhas)
