"""
Classe ItemCarrinho (aula de 10/11).

Fontes para estudar:
- Classes, objetos, atributos e métodos:
  https://docs.python.org/pt-br/3/tutorial/classes.html
- @property (ler um atributo privado):
  https://docs.python.org/pt-br/3/library/functions.html#property
- round (arredondar):
  https://docs.python.org/pt-br/3/library/functions.html#round
- f-string (texto com variáveis):
  https://docs.python.org/pt-br/3/tutorial/inputoutput.html#formatted-string-literals
"""


class ItemCarrinho:
    """
    Uma linha do carrinho: QUAL produto e QUANTAS unidades.

    Quem cria os itens é o Carrinho (composição): o item não existe sozinho.
    """

    def __init__(self, produto, quantidade):
        self.__produto = produto        # associação: ItemCarrinho -> Produto
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    def aumentar(self, quantidade):
        """Soma mais unidades ao item (RN5: produto repetido aumenta a quantidade)."""
        self.__quantidade += quantidade

    def subtotal(self):
        """Preço do produto x quantidade."""
        return round(self.__produto.preco * self.__quantidade, 2)

    def __str__(self):
        return f"{self.__quantidade}x {self.__produto.nome} = R$ {self.subtotal():.2f}"
