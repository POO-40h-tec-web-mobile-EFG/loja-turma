"""
Classe abstrata Pagamento (aula de 12/11).

Fontes para estudar:
- Classe abstrata: ABC e @abstractmethod:
  https://docs.python.org/pt-br/3/library/abc.html
- Atributos privados (__nome) e protegidos (_nome):
  https://docs.python.org/pt-br/3/tutorial/classes.html#private-variables
- Herança:
  https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from abc import ABC, abstractmethod


class Pagamento(ABC):
    """
    CLASSE ABSTRATA: é um modelo para as formas de pagamento.

    Não dá para criar um Pagamento "puro": só as classes filhas (Pix e Cartao).
    """

    def __init__(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento precisa ser maior que zero.")
        # Atributo PROTEGIDO (um sublinhado): a classe e as classes filhas usam
        self._valor = float(valor)

    @property
    def valor(self):
        return self._valor

    @abstractmethod
    def calcular_total(self):
        """Cada forma de pagamento calcula o total do seu jeito."""

    @abstractmethod
    def descricao(self):
        """Nome da forma de pagamento, para mostrar na tela."""
