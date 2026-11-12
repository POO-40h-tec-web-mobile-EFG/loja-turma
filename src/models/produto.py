"""
Classe Produto (aula de 03/11).

Fontes para estudar:
- Classes, objetos, atributos e métodos:
  https://docs.python.org/pt-br/3/tutorial/classes.html
- Construtor __init__:
  https://docs.python.org/pt-br/3/reference/datamodel.html#object.__init__
- Atributos privados (__nome) e protegidos (_nome):
  https://docs.python.org/pt-br/3/tutorial/classes.html#private-variables
- @property (ler um atributo privado):
  https://docs.python.org/pt-br/3/library/functions.html#property
- raise: como gerar um erro:
  https://docs.python.org/pt-br/3/tutorial/errors.html#raising-exceptions
- ValueError:
  https://docs.python.org/pt-br/3/library/exceptions.html#ValueError
- Método __str__ (o que o print mostra):
  https://docs.python.org/pt-br/3/reference/datamodel.html#object.__str__
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""


class Produto:
    """Um produto à venda na loja."""

    def __init__(self, nome, preco, estoque, categoria):
        # Construtor: é chamado quando fazemos Produto("Mouse", 100, 20, eletronicos)
        # Atributos PRIVADOS (dois sublinhados): só a própria classe mexe neles
        self.__nome = nome
        self.__preco = 0.0
        self.__categoria = categoria    # associação: o produto guarda um OBJETO Categoria

        self.alterar_preco(preco)    # RN1: preço maior que zero
        if estoque < 0:                    # RN2: estoque não pode ser negativo
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = estoque

    # metodos construtores propriedades (permitem LER, mas não alterar direto)
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    @property
    def categoria(self):
        return self.__categoria

    # ---------- métodos (ações) ----------
    def alterar_preco(self, valor):
        """Encapsulamento: o preço só muda se for válido."""
        if valor <= 0:
            raise ValueError(f"Preço inválido para {self.__nome}: precisa ser maior que zero.")
        self.__preco = float(valor)

    def tem_estoque(self, quantidade):
        """Responde se existem pelo menos `quantidade` unidades."""
        return self.__estoque >= quantidade

    def baixar_estoque(self, quantidade):
        """Tira unidades do estoque (quando alguém compra)."""
        if not self.tem_estoque(quantidade):
            raise ValueError(
                f"Estoque insuficiente de {self.__nome}: há {self.__estoque} unidade(s)."
            )
        self.__estoque -= quantidade

    def repor_estoque(self, quantidade):
        """Devolve unidades ao estoque."""
        if quantidade <= 0:                # RN2: o estoque nunca fica negativo
            raise ValueError("A quantidade para repor precisa ser maior que zero.")
        self.__estoque += quantidade

    def __str__(self):
        # __str__ define o que aparece quando fazemos print(produto)
        return f"{self.__nome} - R$ {self.__preco:.2f} ({self.__estoque} em estoque) [{self.__categoria}]"