"""
Loja POO - arquivo principal.

Para executar, abra o terminal na pasta do projeto e digite:
    py src/main.py

O programa cria os objetos da loja e mostra, com print, o resultado
de cada regra de negócio (RN1 a RN11). Compare o que aparece na tela
com o valor "esperado" escrito em cada linha.

TESTES DE ERRO: algumas linhas estão desligadas com # na frente.
Elas quebram uma regra de propósito. Para ver a regra funcionando,
tire o # de UMA linha, rode o programa e leia o erro.
Depois coloque o # de volta.

Fontes para estudar:
- import e módulos:
  https://docs.python.org/pt-br/3/tutorial/modules.html
- print e formatação de saída:
  https://docs.python.org/pt-br/3/tutorial/inputoutput.html
- Laço for:
  https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements
- raise: como gerar um erro:
  https://docs.python.org/pt-br/3/tutorial/errors.html#raising-exceptions
- Livro: KEOGH, J.; GIANNINI, M. OOP desmistificado. Alta Books, 2005.
"""

from models.cartao import Cartao
from models.categoria import Categoria
from models.cliente import Cliente
from models.pagamento import Pagamento
from models.pedido import Pedido
from models.pix import Pix
from models.produto import Produto


# ---------- 03/11 - Produto (RN1 e RN2) ----------
print("--- Produto ---")

eletronicos = Categoria("Eletronicos")
notebook = Produto("Notebook", 3500, 5, eletronicos)
mouse = Produto("Mouse", 100, 20, eletronicos)
print(notebook)
print(mouse)

notebook.baixar_estoque(2)
print("Estoque depois de baixar 2 (esperado 3):", notebook.estoque)

notebook.repor_estoque(2)
print("Estoque depois de repor 2 (esperado 5):", notebook.estoque)

# TESTE DE ERRO - RN1: preço precisa ser maior que zero
# Produto("Brinde", -10, 1, eletronicos)

# TESTE DE ERRO - RN2: estoque não pode ser negativo
# Produto("Brinde", 10, -1, eletronicos)

# TESTE DE ERRO - RN2: não dá para baixar mais do que o estoque
# notebook.baixar_estoque(10)


# ---------- 05/11 - Categoria e associação ----------
print("--- Categoria ---")

print("Categoria do notebook (esperado Eletronicos):", notebook.categoria)

# O produto guarda o OBJETO categoria: renomear a categoria muda o produto
eletronicos.renomear("Eletrônicos")
print("Depois de renomear (esperado Eletrônicos):", notebook.categoria)

# TESTE DE ERRO: o nome da categoria não pode ser vazio
# Categoria("")


# ---------- 10/11 - Cliente e Carrinho (RN3, RN4 e RN5) ----------
print("--- Cliente e Carrinho ---")

maria = Cliente("Maria", "maria@email.com")
print(maria)

maria.carrinho.adicionar(notebook, 1)
maria.carrinho.adicionar(mouse, 1)
maria.carrinho.adicionar(mouse, 1)    # RN5: repetido aumenta a quantidade
print(maria.carrinho)
print("Linhas no carrinho (esperado 2):", len(maria.carrinho.itens))
print("Total do carrinho (esperado 3700.0):", maria.carrinho.total())

# TESTE DE ERRO - RN3: e-mail precisa ter @
# maria.atualizar_email("mariaemail.com")

# TESTE DE ERRO - RN4: não pode passar do estoque
# maria.carrinho.adicionar(notebook, 10)


# ---------- 12/11 - Pagamento, Pix e Cartao (RN8, RN9 e RN10) ----------
print("--- Pagamento ---")

pix = Pix(3700)
cartao_3x = Cartao(3700, 3)
cartao_6x = Cartao(3700, 6)

print("RN8 - Pix (esperado 3515.0):", pix.calcular_total())
print("RN9 - Cartão em 3x (esperado 3700.0):", cartao_3x.calcular_total())
print("RN9 - Cartão em 6x (esperado 4070.0):", cartao_6x.calcular_total())

# POLIMORFISMO: a mesma chamada funciona para Pix e para Cartao
pagamentos = [pix, cartao_3x, cartao_6x]
for pagamento in pagamentos:
    print(pagamento.gerar_comprovante())

# TESTE DE ERRO - RN10: cartão aceita de 1 a 12 parcelas
# Cartao(3700, 13)

# TESTE DE ERRO: Pagamento é classe abstrata, não cria objeto
# Pagamento(100)


# ---------- 12/11 - Pedido (RN6, RN7 e RN11) ----------
print("--- Pedido ---")

pedido = Pedido(1, maria, "pix")
print("Total do pedido com Pix (esperado 3515.0):", pedido.total())

pedido.confirmar()
print(pedido)
print("RN11 - Estoque do notebook depois de confirmar (esperado 4):", notebook.estoque)
print("RN11 - Estoque do mouse depois de confirmar (esperado 18):", mouse.estoque)
print("RN7 - Carrinho depois do pedido (esperado Carrinho vazio.):", maria.carrinho)

pedido.cancelar()
print("RN11 - Estoque do notebook depois de cancelar (esperado 5):", notebook.estoque)
print("RN11 - Estoque do mouse depois de cancelar (esperado 20):", mouse.estoque)

# TESTE DE ERRO - RN6: carrinho vazio não fecha pedido
# Pedido(2, maria, "pix")
