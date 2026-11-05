# Loja POO - Ecommerce Programação orientada a objetos

Projeto da disciplina **Programação Orientada a Objetos em Python**.

Durante as aulas, vamos construir **juntos** o "cérebro" (backend) de uma loja virtual: produtos, clientes, carrinho de compras, pagamentos e pedidos. Tudo funciona pelo **terminal**.

Cada aluno trabalha na **sua própria cópia** deste repositório e salva o progresso com **commits**. O histórico de commits mostra o que você fez em cada aula.

> 📘 Login, logout e erros comuns em máquina compartilhada: veja o arquivo `_Orientacoes_e_apoio/Guia-git-github.md`.

---
# AULA 1: CONFIGURAÇÕES
## 1️⃣ Primeira vez: criar a sua cópia (fork)

1. Entre na sua conta do GitHub pelo navegador.
2. Acesse a página: `https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma`, clique no botão **Fork** (canto superior direito) → **Create fork**.
3. Pronto: agora existe `github.com/SEU-USUARIO/loja-turma`. **É nessa cópia que você vai trabalhar.**

## 2️⃣ Primeira vez em cada máquina: baixar o projeto

No VS Code, abra o terminal (**Terminal → Novo Terminal**) e digite um comando por vez. Troque o que está entre aspas pelos seus dados, e `SEU-USUARIO` pelo seu usuário do GitHub:

```powershell
git config --global user.name "Seu Nome Completo"
git config --global user.email "email-da-sua-conta-github@exemplo.com"
cd $HOME\Documents
git clone https://github.com/SEU-USUARIO/loja-turma.git
cd loja-turma
code .
```

## 3️⃣ Executar a loja e rodar os testes

Na janela do VS Code que abriu: **Terminal → Novo Terminal**.

```powershell
py src/main.py
py -m unittest -v
```

- `OK` quer dizer que todos os testes passaram. ✅
- `FAILED` ou `ERROR` quer dizer que ainda falta alguma coisa no código. Leia a mensagem: ela diz qual teste falhou e em qual linha.

## 4️⃣ Fazer alteração incluindo seu nome e subir commit

No VS Code, abra o arquivo na pasta src `main.py` e inclua seu nome em `print("Desenvolvido por: Seu Nome Aqui")`. 

```powershell
git add .
git status
git commit -m "primeiro commit"
git push
```

# AULA 2: CONSTRUINDO CLASSES PRODUTO E CATEGORIA

## 1️⃣ Atualizar, assim que for orientado:

1. Abra o **seu** fork (`github.com/SEU-USUARIO/loja-turma`) e clique em **Sync fork → Update branch**. Isso traz os testes novos que a professora irá inserir.
2. No terminal, dentro da pasta do projeto:
   ```powershell
   git pull
   ```
Vamos criar juntos as classes PRODUTO E CATEGORIA

<img width="551" height="228" alt="image" src="https://github.com/user-attachments/assets/d7a7d9f3-3858-4984-a156-dcfa947441e1" />


## 2️⃣ Durante e no fim da aula: commit e push

```powershell
git add .
git commit -m "Aula 3 - cria classes Categoria e Produto"
git push
```

Ou pelo VS Code: **Source Control** (ícone da forquilha) → escreva a mensagem → **Commit** → **Sync Changes**.

Depois, atualize a página do seu fork no site e confira se o commit apareceu.

# AULA 05-11

Esta aula acontece na **quinta-feira, 05/11, das 18h às 21h45**. Leia este guia **antes** da aula. Quem chegar com o fork atualizado e os testes rodando acompanha a aula inteira sem perder tempo.

**Nesta aula vamos:**

- **Parte 1 (revisão):** revisar as classes `Produto` e `Categoria`. da aula de 03/11 e o diagrama de objetos. Produto já terá o gabarito, Classe categoria vamos construir
- **Parte 2:** criar a classe `Cliente` com validação de e-mail, criar as classes `ItemCarrinho` e `Carrinho` e ligar o cliente ao carrinho, que é a **associação**.



---

## ✅ 0. Antes de começar (checklist)

- [ ] Eu tenho uma conta do GitHub e sei meu usuário.
- [ ] Eu fiz o **fork** do `loja-turma` na minha conta (o endereço deve ser `github.com/MEU-USUARIO/loja-turma`).
- [ ] O Git e o Python estão instalados na minha máquina (`git --version` e `py --version` respondem).
- [ ] Eu tenho o VS Code instalado.
- [ ] Eu sei fazer login e logout seguindo o `_Orientacoes_e_apoio/Guia-git-github.md`.

---

## 🔄 1. Atualizar o seu fork (faça antes da aula)

O professor adiciona os arquivos de teste no repositório da turma. Para recebê-los, você precisa atualizar **o seu fork**.

### 1.1 No site do GitHub

1. Entre na sua conta e abra o **seu** fork: `github.com/MEU-USUARIO/loja-turma`.
2. Confira que o título da página é **MEU-USUARIO/loja-turma**, não `POO-40h-tec-web-mobile-EFG/loja-turma`.
3. Clique no botão **Sync fork**.
4. Clique em **Update branch**.

> Se aparecer **Discard commits** ou uma mensagem de conflito, **não clique**. Veja a seção 5 deste guia.

### 1.2 No computador (terminal do VS Code)

Abra o VS Code na pasta do projeto: **Terminal → Novo Terminal**. Digite **um comando por vez**:

```powershell
cd $HOME\Documents\loja-turma
git status
git pull
py -m unittest -v
```
- `cd $HOME\Documents\loja-turma` é o comando que vai para a pasta do windows \Documents\loja-turma
- `git status` mostra se você tem alterações que ainda não foram salvas no Git. Se aparecer algo, não se preocupe agora: leia a seção 5.
- `git pull` traz as novidades do seu fork para a sua máquina.
- `py -m unittest -v` roda os testes.

**Resultado esperado antes da aula:**

```
Ran 13 tests in 0.001s
OK
```

Se aparecer um **ERROR** em `test_cliente`, isso também é normal, porque a classe `Cliente` ainda não existe. Mas os **13 testes** de `test_categoria` e `test_produto` precisam passar.

---
## 💻 2. Como usar o repositório na sua máquina

### 2.1 Onde fica cada coisa

| Pasta ou arquivo | Para que serve | Você mexe? |
|---|---|---|
| `src/main.py` | Arquivo principal. É ele que roda com `py src/main.py` | **Sim** |
| `src/models/` | As classes da loja (uma classe por arquivo) | **Sim** |
| `tests/` | Testes automáticos | **Não** |
| `_Orientacoes_e_apoio/` | Guia de Git e materiais de apoio | Não |
| `README.md` | Este roteiro e as aulas | Não |

> Escreva **somente** dentro de `src/`. Se você mexer em `tests/`, o **Sync fork** das próximas aulas vai dar conflito.

### 2.2 Arquivos que você vai criar hoje

```
src/
├── main.py
└── models/
    ├── __init__.py
    ├── categoria.py       (revisar)
    ├── produto.py         (revisar)
    ├── cliente.py         (criar)
    ├── item_carrinho.py   (criar)
    └── carrinho.py        (criar)
```

### 2.3 Comandos do dia a dia

| Comando | O que faz |
|---|---|
| `py src/main.py` | Roda o programa |
| `py -m unittest -v` | Roda os testes |
| `git status` | Mostra o que mudou |
| `git add src` | Prepara os arquivos da pasta `src` para o commit |
| `git commit -m "mensagem"` | Salva o progresso com um nome (veja a seção 4) |
| `git push` | Envia o commit para o **seu fork** no GitHub |

---

## 🎬 3. Roteiro da aula de hoje

### Parte 1: revisão (cerca de 20 min)

Vamos revisar a aula de 03/11 com perguntas. Pense nas respostas:

1. O que é uma **classe**? E um **objeto**?
2. O que é um **atributo**? E um **método**?
3. O que faz o **construtor** (`__init__`)?
4. O que quer dizer `self.__preco`?
5. Por que o `preco` tem `@property`, mas não tem como alterar direto?
6. Qual a diferença entre o **diagrama de classes** e o **diagrama de objetos**?

**Você também vai desenhar um diagrama de objetos no caderno:**

```
notebook : Produto                  eletronicos : Categoria
  nome   = "Notebook"        ───►    nome = "Eletrônicos"
  preco  = 3500.00
  estoque = 5
```

### Parte 2: construção (o resto da aula)

Vamos construir, passo a passo, junto com o professor. Acompanhe e digite cada bloco no seu computador:

| Bloco | O que vamos construir | Arquivo |
|---|---|---|
| 2.1 | Classe `Cliente` sem validação, e ver o problema | `src/models/cliente.py` |
| 2.2 | Validação do e-mail (RN3) com `atualizar_email()` | `src/models/cliente.py` |
| 2.3 | `__str__` do cliente e troca de e-mail | `src/models/cliente.py` |
| 2.4 | Classe `ItemCarrinho` (produto e quantidade) | `src/models/item_carrinho.py` |
| 2.5 | Classe `Carrinho`: adicionar, total, regras RN4 e RN5 | `src/models/carrinho.py` |
| 2.6 | Remover, esvaziar e mostrar o carrinho | `src/models/carrinho.py` |
| 2.7 | Ligar o `Cliente` ao `Carrinho`: a **associação** | `src/models/cliente.py` |
| 2.8 | Testar tudo no `main.py` | `src/main.py` |

**Regras de negócio que vamos usar:**

- **RN3:** o e-mail precisa ter `@`.
- **RN4:** não pode colocar no carrinho mais do que o estoque do produto.
- **RN5:** se o produto já está no carrinho, aumenta a quantidade, em vez de criar outra linha.

### Testes esperados ao longo da aula

| Momento | Resultado esperado |
|---|---|
| Depois de atualizar o fork | 13 testes OK (categoria e produto) |
| Depois de criar o `Cliente` | 16 testes OK |
| Depois de criar o `Carrinho` e receber a nova versão de `test_cliente.py` e `test_carrinho.py` | **25 testes OK** |

---
## 🏷️ 4. Padrão de nome dos commits (obrigatório)

As avaliações levam em conta os **commits** de cada aluno. Por isso, **todo commit desta aula segue o mesmo padrão**:

```
Aula 05-11 - <o que você fez>
```

### 4.1 Os commits desta aula

Faça **um commit para cada marco**, quando os testes do marco passarem:

| Quando fazer | Mensagem do commit |
|---|---|
| Se você corrigiu algo na revisão | `Aula 05-11 - revisão Produto e Categoria` |
| Quando o `Cliente` funcionar (16 testes OK) | `Aula 05-11 - cria classe Cliente com validação de e-mail` |
| Quando o `Carrinho` e o `ItemCarrinho` funcionarem | `Aula 05-11 - cria classes ItemCarrinho e Carrinho` |
| Quando o `Cliente` tiver o carrinho (main.py roda sem erro) | `Aula 05-11 - associa Cliente ao Carrinho` |

### 4.2 Seu nome no commit

O commit sai com o **nome que está configurado no Git**. Confira se ele é o seu nome completo, igual ao do seu perfil do GitHub:

```powershell
git config --global user.name
git config --global user.email
```

Se estiver errado, configure:

```powershell
git config --global user.name "Seu Nome Completo"
git config --global user.email "email-da-sua-conta-github@exemplo.com"
```

> Em máquina compartilhada, faça o **logout** no fim da aula (seção 6). Não deixe o nome de outra pessoa configurado.

### 4.3 Exemplo de um commit completo

```powershell
git add src
git commit -m "Aula 05-11 - cria classe Cliente com validação de e-mail"
git push
```

**Não use** `git add .` se aparecer uma pasta chamada `__pycache__` na lista do `git status`. Ela é criada pelo Python e não faz parte do projeto. Use `git add src` e confirme que `tests/` não aparece como modificado.

---

## 🧩 5. Erros comuns na atualização do fork e como resolver

| O que aparece | Por que acontece | Como resolver |
|---|---|---|
| No site: **"This branch is out-of-date"** ou **"Sync fork"** com botão **Update branch** | Seu fork está atrás do repositório da turma. | Clique em **Update branch**. É o esperado. |
| No site: **"This branch has conflicts"** ou **Discard commits** | Você mexeu em arquivos que não deveria ou em outro lugar do projeto. | **Não clique em Discard commits** sem ajuda. Chame o professor. |
| `git pull` abre uma tela estranha pedindo uma mensagem de merge | O Git precisa de uma mensagem para unir as versões. | No VS Code, feche a aba. No terminal (vim), digite `:wq` e Enter. |
| `error: Your local changes would be overwritten by merge` | Você tem alterações salvas que o `git pull` vai substituir. | Digite `git add src` e `git commit -m "Aula 05-11 - alterações antes de atualizar"`. Depois, `git pull`. |
| `! [rejected]` ou `fetch first` no `git push` | Seu fork tem algo novo que você ainda não baixou. | Digite `git pull` e depois `git push`. |
| `Permission denied` ou erro 403 no `git push` | Você clonou o repositório **da turma** (`POO-40h-tec-web-mobile-EFG`) em vez do **seu fork**. | Veja o passo abaixo: "Clonei o repositório errado". |
| `git` não é reconhecido | O Git não está instalado nesta máquina. | Use uma máquina do laboratório, ou faça dupla com um colega. |
| `py` não é reconhecido | O Python não está instalado ou o comando é diferente. | Tente `python3 src/main.py`. Se abrir a Microsoft Store, faça dupla com um colega. |
| `ModuleNotFoundError: No module named 'models'` | Você rodou o comando dentro da pasta errada. | Rode sempre **a partir da pasta do projeto** (`loja-turma`), não de dentro de `src`. |
| `ERROR` em `produto` depois do `git pull` | A pasta `src` ficou com arquivos de outra versão. | Chame o professor. Não apague nada sem ajuda. |

### 5.1 Clonei o repositório errado

Verifique qual repositório está conectado:

```powershell
git remote -v
```

- Se aparecer `POO-40h-tec-web-mobile-EFG/loja-turma`, você está no repositório da turma. **Não envie código para lá.**
- O certo é `MEU-USUARIO/loja-turma`.

**Como corrigir:**

1. Copie a pasta `src` para um lugar seguro, por exemplo `$HOME\Documents\backup-src`.
2. Clone o **seu** fork:
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/MEU-USUARIO/loja-turma.git loja-turma-meu
   ```
3. Copie a pasta `src` de volta para `loja-turma-meu`, substituindo os arquivos.
4. Dentro de `loja-turma-meu`, faça o commit e o push com o padrão da seção 4.

### 5.2 Perdi o código ou a pasta sumiu

Se a sua pasta do projeto não está mais na máquina:

1. Abra o **seu** fork no site e clique em **Sync fork → Update branch**.
2. Clone de novo:
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/MEU-USUARIO/loja-turma.git
   ```
3. Rode o `main.py` para conferir: `py src/main.py`.

> Se você já fez commit e push antes, todo o seu código volta inteiro pelo clone.

---
## 🏁 6. Ao final da aula: commit, push e logout

1. **Último commit da aula** (depois que o main.py rodar sem erro):
   ```powershell
   git add src
   git commit -m "Aula 05-11 - associa Cliente ao Carrinho"
   git push
   ```
2. **Confira no site:** abra o **seu** fork, clique em **commits** e veja se os commits aparecem com o nome certo.
3. **Logout completo**, seguindo a seção **"4. Indo embora: logout"** do `_Orientacoes_e_apoio/Guia-git-github.md`:
   - Saia da conta no VS Code (ícone de **Contas**).
   - Saia do GitHub no navegador.
   - Apague o nome e o e-mail do Git, se a máquina for compartilhada:
   ```powershell
   git config --global --unset user.name
   git config --global --unset user.email
   ```

---

## ❓ 7. Dúvidas frequentes

**Preciso terminar tudo para ter presença?**
Não. Faça o que der. Os commits de cada marco já contam, e o que faltar pode ser enviado depois da aula.

**Posso copiar o código de um colega?**
Não. Cada aluno escreve o próprio código. Use o roteiro e os exemplos do professor. Se travar, peça ajuda ao professor.

**Esqueci de fazer commit durante a aula. E agora?**
Faça o commit antes de ir embora, mesmo que o código ainda não esteja completo. Use a mensagem do marco mais próximo, por exemplo `Aula 05-11 - cria classe Cliente com validação de e-mail`.

**Se eu perder a aula?**
Siga este guia, faça o **Sync fork**, o `git pull` e o commit com o padrão da seção 4. Depois, procure o professor para tirar as dúvidas.




# SEMPRE
## 1️⃣ Antes de ir embora: logout

Máquina compartilhada! Siga a seção **"4. Indo embora: logout"** do `Guia-git-github.md`: saia da conta no VS Code, apague nome e e-mail do Git, remova a credencial do Windows e saia do GitHub no navegador.
VEJA: `https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma/blob/main/_Orientacoes_e_apoio/Guia-git-github.md`
---
# PARA SABER MAIS:
## 📁 O que tem em cada pasta

| Pasta | Para que serve |
|---|---|
| `src/main.py` | Arquivo principal: é ele que a gente executa |
| `src/models/` | As classes da loja (uma classe por arquivo que vamos construir) |
| `tests/` | Testes automáticos. **Não mexa nesta pasta**: só vamos rodar os testes e no final vamos explicar a construção dos testes |
| `codigo-das-aulas/` | para construir em conjunto |
| `_Orientacoes_e_apoio/` | Guia de Git e materiais de apoio |

## ⚠️ Combinados

- Escreva o seu código **dentro da pasta `src/`**. Não altere `tests/` nem `codigo-das-aulas/`.
- Faça commit **pelo menos no fim de cada aula**, com uma mensagem que diga o que você fez (ex.: `Aula 4 - cria classe Cliente`).
- Faltou ou perdeu o código? Faça o **Sync fork** e o `git pull`, copie a pasta `src` da última aula que está em `codigo-das-aulas/` para a sua pasta `src`, e faça commit e push.
- **Quem entra, sai:** sempre faça o logout antes de ir embora.
