"""
Classe Categoria (aula de 05/11).

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
- Método __str__ (o que o print mostra):
  https://docs.python.org/pt-br/3/reference/datamodel.html#object.__str__
"""


class Categoria:
    """Grupo de produtos da loja (ex.: Eletrônicos, Livros)."""

    def __init__(self, nome):
        # Atributo PRIVADO (dois sublinhados): só a própria classe mexe nele
        self.__nome = ""
        self.renomear(nome)    # usa a mesma validação do renomear()

    # Propriedade: permite LER o nome, mas não alterar direto
    @property
    def nome(self):
        return self.__nome

    def renomear(self, nome):
        """Troca o nome da categoria. O nome não pode ser vazio."""
        nome = nome.strip()
        if nome == "":
            raise ValueError("O nome da categoria não pode ser vazio.")
        self.__nome = nome

    def __str__(self):
        # __str__ define o que aparece quando fazemos print(categoria)
        return self.__nome
