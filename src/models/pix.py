"""
Classe Pix (aula de 12/11).

Fontes para estudar:
- Herança:
  https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance
- Herança múltipla:
  https://docs.python.org/pt-br/3/tutorial/classes.html#multiple-inheritance
- round (arredondar):
  https://docs.python.org/pt-br/3/library/functions.html#round
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from models.comprovante import Comprovante
from models.pagamento import Pagamento


class Pix(Pagamento, Comprovante):
    """
    HERANÇA: Pix É UM Pagamento.
    INTERFACE: Pix também implementa o contrato Comprovante.
    """

    DESCONTO = 0.05    # RN8: Pix tem 5% de desconto

    def calcular_total(self):
        # SOBREPOSIÇÃO: mesmo nome do método da classe mãe, cálculo próprio
        return round(self._valor * (1 - Pix.DESCONTO), 2)

    def descricao(self):
        return "Pix (5% de desconto)"

    def gerar_comprovante(self):
        return f"Comprovante Pix: R$ {self.calcular_total():.2f} pagos à vista."
