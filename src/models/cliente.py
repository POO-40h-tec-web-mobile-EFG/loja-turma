"""
Classe Cliente (aula de 10/11).

Fontes para estudar:
- Classes, objetos, atributos e métodos:
  https://docs.python.org/pt-br/3/tutorial/classes.html
- Atributos privados (__nome) e protegidos (_nome):
  https://docs.python.org/pt-br/3/tutorial/classes.html#private-variables
- @property (ler um atributo privado):
  https://docs.python.org/pt-br/3/library/functions.html#property
- Listas: append e remove:
  https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists
- raise: como gerar um erro:
  https://docs.python.org/pt-br/3/tutorial/errors.html#raising-exceptions
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from models.carrinho import Carrinho


class Cliente:
    """Pessoa que compra na loja."""

    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = ""
        self.atualizar_email(email)      # RN3: e-mail precisa ter @
        self.__carrinho = Carrinho()     # associação: o cliente ganha um carrinho
        self.__pedidos = []              # lista dos pedidos que o cliente confirmou

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def carrinho(self):
        return self.__carrinho

    @property
    def pedidos(self):
        # Devolve uma CÓPIA da lista, para ninguém alterar a original por fora
        return list(self.__pedidos)

    def atualizar_email(self, valor):
        """Encapsulamento: só aceita e-mail com @ (RN3)."""
        valor = valor.strip()
        if "@" not in valor:
            raise ValueError(f"E-mail inválido: {valor}")
        self.__email = valor.lower()

    def adicionar_pedido(self, pedido):
        """Guarda um pedido confirmado na lista do cliente."""
        self.__pedidos.append(pedido)

    def __str__(self):
        return f"{self.__nome} <{self.__email}>"
