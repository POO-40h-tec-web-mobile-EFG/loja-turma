# Loja POO - Ecommerce Programação Orientada a Objetos

Projeto da disciplina **Programação Orientada a Objetos com Python**.
https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma

Durante as aulas, vamos construir **juntos** o "cérebro" (backend) de uma loja virtual: produtos, clientes, carrinho de compras, pagamentos e pedidos. Tudo funciona pelo **terminal**.

Cada aluno trabalha na **sua própria cópia** deste repositório e salva o progresso com **commits**. O histórico de commits mostra o que você fez em cada aula. Quem não conseguir enviar pelo GitHub pode enviar a atividade **por e-mail**, conforme a orientação da professora.

> 📘 Login, logout e erros comuns em máquina compartilhada: veja o arquivo `_Orientacoes_e_apoio/Guia-git-github.md`.

---


## Configuração (primeira vez)

### 1. Criar a sua cópia (fork)

1. Entre na sua conta do GitHub pelo navegador.
2. Acesse a página `https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma`, clique no botão **Fork** (canto superior direito) → **Create fork**.
3. Pronto: agora existe `github.com/SEU-USUARIO/loja-turma`. **É nessa cópia que você vai trabalhar.**

### 2. Baixar o projeto (primeira vez em cada máquina)

No VS Code, abra o terminal (**Terminal → Novo Terminal**) e digite um comando por vez. Troque o que está entre aspas pelos seus dados, e `SEU-USUARIO` pelo seu usuário do GitHub:

```powershell
git config --global user.name "SEU USUARIO"
git config --global user.email "email-da-sua-conta-github@exemplo.com"
cd $HOME\Documents
git clone https://github.com/SEU-USUARIO/loja-turma.git
cd loja-turma
code .
```

### 3. Executar a loja

Na janela do VS Code que abriu: **Terminal → Novo Terminal**.

```powershell
py src/main.py
```

O `main.py` mostra as **verificações** de cada regra de negócio. Cada linha traz o valor **esperado** e o valor que o seu código calculou:

```
Total do carrinho (esperado 3700.0): 3700.0
```

- Se os dois valores são iguais, a regra está funcionando. ✅
- Se são diferentes, ou se aparece uma mensagem de erro (`Traceback`), ainda falta alguma coisa no código. Leia a mensagem: ela diz em qual linha parou.

**Testes de erro:** no `main.py` há linhas desligadas com `#` na frente, como `# Produto("Brinde", -10, 1, eletronicos)`. Elas quebram uma regra de propósito. Tire o `#` de **uma** linha, rode o programa e leia o `ValueError`: é a regra recusando o dado inválido. Depois coloque o `#` de volta.

---

## Em toda aula: atualizar o seu fork

1. Abra o **seu** fork (`github.com/SEU-USUARIO/loja-turma`) e clique em **Sync fork → Update branch**.
2. No terminal, dentro da pasta do projeto, digite **um comando por vez**:

```powershell
cd $HOME\Documents\loja-turma
git status
git pull
py src/main.py
```

> Se aparecer **Discard commits** ou uma mensagem de conflito, **não clique**. Veja a seção "Erros comuns".

---

## Como o projeto está organizado

| Pasta ou arquivo | Para que serve | Você mexe? |
|---|---|---|
| `src/main.py` | Arquivo principal. É ele que roda com `py src/main.py` | **Sim** |
| `src/models/` | As classes da loja (uma classe por arquivo) | **Sim** |
| `diagramas/` | Diagramas de classes, de objetos, de casos de uso e de sequência | Não |
| `_Orientacoes_e_apoio/` | Guia de Git e materiais de apoio | Não |
| `README.md` | Este roteiro | Não |

```
src/
├── main.py
└── models/
    ├── __init__.py
    ├── produto.py
    ├── categoria.py 
    ├── cliente.py 
    ├── item_carrinho.py  
    ├── carrinho.py     
    ├── pagamento.py      
    ├── comprovante.py  
    ├── pix.py            
    ├── cartao.py         
    └── pedido.py      
```

### Comandos do dia a dia

| Comando | O que faz |
|---|---|
| `py src/main.py` | Roda o programa e mostra as verificações |
| `git status` | Mostra o que mudou |
| `git add .` | Prepara os arquivos todos os arquivos para o commit |
| `git commit -m "mensagem"` | Salva o progresso (commit) com um nome |
| `git push -u origin aula_DD-MM` | Envia o commit para sua branch **aula** no seu usuário GitHub |

---

## 📐 Diagramas

Os diagramas ficam na pasta `diagramas/` e aparecem desenhados quando você abre o arquivo no site do GitHub.

| Diagrama | O que mostra | Aula |
|---|---|---|
| [Classes](diagramas/diagrama-classes.md) | As peças do sistema: classes, atributos, métodos e ligações
| [Objetos](diagramas/diagrama-objeto.md) | Uma "foto" dos objetos criados e dos valores que eles guardam
| [Casos de uso](diagramas/diagrama-caso-uso.md) | O que o cliente consegue fazer na loja
| [Sequência](diagramas/diagrama-sequencia.md) | A ordem das mensagens na finalização do pedido 


---

## 📏 Regras de negócio

Cada regra é conferida no `main.py`.

| Regra | Descrição | Encontro |
|---|---|---|
| RN1 | Preço do produto maior que zero |
| RN2 | Estoque nunca negativo | 
| RN3 | E-mail do cliente precisa ter `@` | 
| RN4 | Carrinho não passa do estoque do produto |
| RN5 | Produto repetido no carrinho soma a quantidade, em vez de criar outra linha |
| RN6 | Pedido não fecha com carrinho vazio |
| RN7 | Carrinho esvazia depois do pedido |
| RN8 | Pix tem 5% de desconto |
| RN9 | Cartão acima de 3 parcelas: 10% a mais |
| RN10 | Cartão de 1 a 12 parcelas |
| RN11 | Confirmar o pedido baixa o estoque; cancelar devolve |

---

## Padrão de nome dos commits (obrigatório)

Todo commit segue o mesmo padrão, com a **data da aula**:

```
Aula DD-MM - <o que você fez>
```

Exemplo de um commit completo:

```powershell
git add src
git commit -m "Aula 12-11 - cria Pagamento, Pix, Cartao e Pedido"
git push
```

Ou pelo VS Code: **Source Control** → escreva a mensagem → **Commit** → **Sync Changes**. Depois, atualize a página do seu fork no site e confira se o commit apareceu.

O commit sai com o **nome que está configurado no Git**. Confira se ele é o seu nome completo:

```powershell
git config --global user.name
git config --global user.email
```

---

## Avaliação

| O que conta | Quando |
|---|---|
| Envio das atividades de cada aula (commit no GitHub ou e-mail) | Todas as aulas |
| Atividade assíncrona: polimorfismo e código comentado | Até 14/11 |
| Apresentação individual de 10 a 15 min | 17/11 |
| Questionário impresso (10 questões) e envio final do projeto | 19/11 |
| Questionário online de recuperação, só para quem for convocado | 24/11 |

---

## Erros comuns e como resolver

| O que aparece | Por que acontece | Como resolver |
|---|---|---|
| No site: **"This branch is out-of-date"** com botão **Update branch** | Seu fork está atrás do repositório da turma. | Clique em **Update branch**. É o esperado. |
| No site: **"This branch has conflicts"** ou **Discard commits** | Você alterou um arquivo que a professora também alterou. | **Não clique em Discard commits** sem ajuda. Chame a professora. |
| `git pull` abre uma tela estranha pedindo uma mensagem de merge | O Git precisa de uma mensagem para unir as versões. | No VS Code, feche a aba. No terminal (vim), digite `:wq` e Enter. |
| `error: Your local changes would be overwritten by merge` | Você tem alterações que o `git pull` vai substituir. | Digite `git add src` e `git commit -m "Aula DD-MM - alterações antes de atualizar"`. Depois, `git pull`. |
| `! [rejected]` ou `fetch first` no `git push` | Seu fork tem algo novo que você ainda não baixou. | Digite `git pull` e depois `git push`. |
| `Permission denied` ou erro 403 no `git push` | Você clonou o repositório **da turma** em vez do **seu fork**. | Veja "Clonei o repositório errado", abaixo. |
| `git` não é reconhecido | O Git não está instalado nesta máquina. | Use uma máquina do laboratório, ou faça dupla com um colega. |
| `py` não é reconhecido | O Python não está instalado ou o comando é diferente. | Tente `python3 src/main.py`. Se abrir a Microsoft Store, faça dupla com um colega. |
| `ModuleNotFoundError: No module named 'models'` | Você rodou o comando dentro da pasta errada. | Rode sempre **a partir da pasta do projeto** (`loja-turma`), com `py src/main.py`. |

### Clonei o repositório errado

Verifique qual repositório está conectado:

```powershell
git remote -v
```

- Se aparecer `POO-40h-tec-web-mobile-EFG/loja-turma`, você está no repositório da turma. **Não envie código para lá.**
- O certo é `SEU-USUARIO/loja-turma`.

**Como corrigir:**

1. Copie a pasta `src` para um lugar seguro, por exemplo `$HOME\Documents\backup-src`.
2. Clone o **seu** fork:
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/SEU-USUARIO/loja-turma.git loja-turma-meu
   ```
3. Copie a pasta `src` de volta para `loja-turma-meu`, substituindo os arquivos.
4. Dentro de `loja-turma-meu`, faça o commit e o push com o padrão de commits.

### Perdi o código ou a pasta sumiu

1. Abra o **seu** fork no site e clique em **Sync fork → Update branch**.
2. Clone de novo:
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/SEU-USUARIO/loja-turma.git
   ```
3. Rode o `main.py` para conferir: `py src/main.py`.

> Se você já fez commit e push antes, todo o seu código volta inteiro pelo clone.

---

## Ao final de toda aula: commit, push e logout, ou enviar por email

1. **Último commit da aula**, com o padrão de commits, e `git push` (ou envio por e-mail).
2. **Confira no site:** abra o **seu** fork, clique em **commits** e veja se os commits aparecem com o nome certo.
3. **Logout completo**, seguindo a seção **"4. Indo embora: logout"** do `_Orientacoes_e_apoio/Guia-git-github.md`:
   - Saia da conta no VS Code (ícone de **Contas**).
   - Saia do GitHub no navegador.
   - Apague o nome e o e-mail do Git e a credencial do Windows:
   ```powershell
   git config --global --unset user.name
   git config --global --unset user.email
   cmdkey /delete:git:https://github.com
   ```
   OU
   
4. Enviar por e-mail

   - No Explorador de Arquivos, abra a pasta `loja-turma`.
   - Clique com o botão direito na pasta `src` > **Enviar para** > **Pasta compactada**.
   - Renomeie o arquivo para `src-SEU-NOME-aula-DD-MM.zip`.
   - Envie o arquivo com estes dados:

   | Campo | O que escrever |
   |---|---|
   | Para | `stela.edu@outlook.com` |
   | Assunto | `POO - Atividade aula DD-MM - SEU NOME` |
   | Anexo | `src-SEU-NOME-aula-DD-MM.zip` |


**Quem entra, sai:** a máquina é compartilhada.

---

## Dúvidas frequentes

**Preciso terminar tudo na aula?**
Não. Faça o que der. Os commits de cada aula já contam, e o que faltar pode ser enviado depois.

**Posso copiar o código de um colega?**
Não. Cada aluno escreve o próprio código, e na apresentação de 17/11 você explica o seu. Se travar, peça ajuda à professora.

**Esqueci de fazer commit durante a aula. E agora?**
Faça o commit antes de ir embora, mesmo que o código ainda não esteja completo.

**Não consegui enviar pelo GitHub. E agora?**
Envie a atividade por e-mail, conforme a orientação da professora.

**Se eu perder a aula?**
Siga o roteiro da aula neste guia, faça o **Sync fork**, o `git pull` e o commit com o padrão de commits. Depois, procure a professora para tirar as dúvidas.

---

## Referências

- CHACON, S.; STRAUB, B. **Pro Git**. 2. ed. Apress, 2014. Disponível em: https://git-scm.com/book/pt-br/v2.
- DOWNEY, A. B. **Pense em Python**: pense como um cientista da computação. São Paulo: Novatec, 2016.
- GUEDES, G. T. A. **UML 2**: uma abordagem prática. 3. ed. São Paulo: Novatec, 2018.
- KEOGH, J.; GIANNINI, M. **OOP desmistificado**: programação orientada a objetos. Rio de Janeiro: Alta Books, 2005.
- PYTHON SOFTWARE FOUNDATION. **O tutorial Python**. Disponível em: https://docs.python.org/pt-br/3/tutorial/.
