"""
Interface Comprovante (aula de 12/11).

Fontes para estudar:
- Classe abstrata: ABC e @abstractmethod:
  https://docs.python.org/pt-br/3/library/abc.html
- Herança múltipla:
  https://docs.python.org/pt-br/3/tutorial/classes.html#multiple-inheritance
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from abc import ABC, abstractmethod


class Comprovante(ABC):
    """
    INTERFACE: só define um contrato, sem atributos e sem código pronto.

    Quem implementa esta interface "tem a capacidade de" gerar um comprovante.
    Diferença para a classe abstrata Pagamento: lá a relação é "é um"
    (Pix É UM Pagamento) e a classe pode ter atributos e métodos prontos.
    """

    @abstractmethod
    def gerar_comprovante(self):
        """Devolve o texto do comprovante."""
