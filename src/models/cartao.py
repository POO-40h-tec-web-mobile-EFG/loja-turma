"""
Classe Cartao (aula de 12/11).

Fontes para estudar:
- Herança:
  https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance
- super():
  https://docs.python.org/pt-br/3/library/functions.html#super
- Parâmetro opcional (valor padrão):
  https://docs.python.org/pt-br/3/tutorial/controlflow.html#default-argument-values
- raise: como gerar um erro:
  https://docs.python.org/pt-br/3/tutorial/errors.html#raising-exceptions
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from models.comprovante import Comprovante
from models.pagamento import Pagamento


class Cartao(Pagamento, Comprovante):
    """
    HERANÇA: Cartao É UM Pagamento.
    INTERFACE: Cartao também implementa o contrato Comprovante.
    """

    JUROS = 0.10    # RN9: acima de 3 parcelas, o total fica 10% maior

    def __init__(self, valor, parcelas=1):
        # parcelas=1 é um parâmetro OPCIONAL: simula a sobrecarga em Python.
        # Cartao(100) e Cartao(100, 6) funcionam com o mesmo construtor.
        super().__init__(valor)    # super() chama o construtor de Pagamento
        if parcelas < 1 or parcelas > 12:    # RN10: de 1 a 12 parcelas
            raise ValueError("O cartão aceita de 1 a 12 parcelas.")
        self.__parcelas = parcelas

    @property
    def parcelas(self):
        return self.__parcelas

    def calcular_total(self):
        # SOBREPOSIÇÃO: mesmo nome do método da classe mãe, cálculo próprio
        if self.__parcelas > 3:    # RN9
            return round(self._valor * (1 + Cartao.JUROS), 2)
        return round(self._valor, 2)

    def descricao(self):
        return f"Cartão em {self.__parcelas}x"

    def gerar_comprovante(self):
        valor_parcela = round(self.calcular_total() / self.__parcelas, 2)
        return (
            f"Comprovante Cartão: R$ {self.calcular_total():.2f} "
            f"em {self.__parcelas}x de R$ {valor_parcela:.2f}."
        )
