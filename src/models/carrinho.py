"""
Classe Carrinho (aula de 10/11).

Fontes para estudar:
- Listas: append e remove:
  https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists
- Laço for:
  https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements
- Parâmetro opcional (valor padrão):
  https://docs.python.org/pt-br/3/tutorial/controlflow.html#default-argument-values
- Atributos privados (__nome) e protegidos (_nome):
  https://docs.python.org/pt-br/3/tutorial/classes.html#private-variables
- raise: como gerar um erro:
  https://docs.python.org/pt-br/3/tutorial/errors.html#raising-exceptions
- Livro: GUEDES, G. T. A. UML 2: uma abordagem prática. 3. ed. Novatec, 2018.
"""

from models.item_carrinho import ItemCarrinho


class Carrinho:
    """
    Carrinho de compras de um cliente.

    COMPOSIÇÃO: o carrinho é quem cria e guarda os objetos ItemCarrinho.
    Os itens ficam numa LISTA de objetos.
    """

    def __init__(self):
        self.__itens = []    # lista de objetos ItemCarrinho

    @property
    def itens(self):
        # Devolve uma CÓPIA da lista, para ninguém alterar a original por fora
        return list(self.__itens)

    def __buscar_item(self, produto):
        """Método PRIVADO: procura o item de um produto na lista."""
        for item in self.__itens:
            if item.produto is produto:
                return item
        return None

    def adicionar(self, produto, quantidade=1):
        """Coloca um produto no carrinho (ou aumenta a quantidade, se já estiver lá)."""
        if quantidade <= 0:
            raise ValueError("A quantidade precisa ser maior que zero.")

        item = self.__buscar_item(produto)
        quantidade_total = quantidade
        if item is not None:
            quantidade_total += item.quantidade

        if not produto.tem_estoque(quantidade_total):        # RN4
            raise ValueError(
                f"Só há {produto.estoque} unidade(s) de {produto.nome} em estoque."
            )

        if item is not None:
            item.aumentar(quantidade)                          # RN5
        else:
            self.__itens.append(ItemCarrinho(produto, quantidade))

    def remover(self, produto):
        """Tira um produto do carrinho."""
        item = self.__buscar_item(produto)
        if item is None:
            raise ValueError(f"{produto.nome} não está no carrinho.")
        self.__itens.remove(item)

    def total(self):
        """Soma os subtotais de todos os itens."""
        soma = 0.0
        for item in self.__itens:
            soma += item.subtotal()
        return round(soma, 2)

    def esta_vazio(self):
        return len(self.__itens) == 0

    def limpar(self):
        """Esvazia o carrinho (RN7: depois de confirmar o pedido)."""
        self.__itens = []

    def __str__(self):
        if self.esta_vazio():
            return "Carrinho vazio."
        linhas = []
        for item in self.__itens:
            linhas.append(str(item))
        linhas.append(f"TOTAL: R$ {self.total():.2f}")
        return "\n".join(linhas)
