# Guia: como enviar a atividade para a professora

Repositório da turma: <https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma>

Escolha **um** caminho:

- [Via GitHub](#via-github): para quem fez o fork.
- [Via e-mail](#via-e-mail): para quem não conseguiu usar o GitHub.

---

# VIA GITHUB

> **Regra de ouro:** você só envia (`push`) para o **seu** repositório (`origin`), sempre em uma **branch da aula**.
> Nunca envie para o repositório da professora. Nunca faça `merge` nem `pull request`.

| Nome | De quem é | O que você faz |
|---|---|---|
| `origin` | **Seu** fork: `SEU-USUARIO/loja-turma` | Envia a atividade (`push`) |
| `upstream` | Professora: `POO-40h-tec-web-mobile-EFG/loja-turma` | Só baixa as novidades (`fetch`) |

## 1. Abra o projeto no VS Code

1. **File** > **Open Folder** > selecione a pasta `loja-turma`.
2. Abra o terminal: menu **Terminal** > **New Terminal**.
3. Confira se a linha do terminal termina em `\loja-turma>`.

> **Ainda não tem a pasta?** Veja [Primeira vez](#primeira-vez-fork-e-clone), no fim desta parte.

## 2. Confira os endereços

```powershell
git remote -v
```

O resultado deve ser assim, com o seu usuário no lugar de `SEU-USUARIO`:

```text
origin    https://github.com/SEU-USUARIO/loja-turma.git (fetch)
origin    https://github.com/SEU-USUARIO/loja-turma.git (push)
upstream  https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git (fetch)
upstream  SEM_PUSH (push)
```

Se o `upstream` não aparecer, ou se a última linha não mostrar `SEM_PUSH`, rode um comando por vez:

```powershell
git remote add upstream https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git
```

```powershell
git remote set-url --push upstream SEM_PUSH
```

*O `SEM_PUSH` é uma trava: ela impede qualquer envio para o repositório da professora.*

> ⚠️ **Pare** se aparecer `POO-40h-tec-web-mobile-EFG` na linha do `origin`. Veja a tabela de [problemas](#problemas-comuns).

## 3. Crie a branch da aula

Troque `DD-MM` pela data da aula. Exemplo para 12 de novembro: `aula_12-11`.

```powershell
git fetch upstream
```

```powershell
git checkout -b aula_DD-MM --no-track upstream/main
```

- **`git fetch upstream`** baixa as novidades da professora, sem mexer nos seus arquivos.
- **`git checkout -b ...`** cria a sua branch da aula a partir da versão mais nova da professora.

Confira: o **canto inferior esquerdo** do VS Code deve mostrar `aula_DD-MM`.

*Como a branch nasce da versão da professora, não existe conflito e não é preciso `merge`.*

## 4. Faça a atividade

1. Siga o roteiro da aula no `README.md`.
2. Escreva o código **somente** na pasta `src`.
3. Teste:

```powershell
py src/main.py
```

> ⚠️ Não edite o `README.md` nem a pasta `_Orientacoes_e_apoio`: eles são da professora.

## 5. Envie para o seu repositório

Rode um comando por vez:

```powershell
git add src
```

```powershell
git commit -m "Aula DD-MM - o que você fez"
```

```powershell
git push -u origin aula_DD-MM
```

Confira no site: abra `github.com/SEU-USUARIO/loja-turma`, clique no botão das branches e escolha `aula_DD-MM`. O seu commit deve aparecer.

> 💡 O site vai oferecer o botão **Compare & pull request**. **Não clique.** A professora confere a atividade direto na sua branch.

## Resumo rápido

```powershell
git remote -v
git fetch upstream
git checkout -b aula_DD-MM --no-track upstream/main
# ... faça a atividade na pasta src ...
git add src
git commit -m "Aula DD-MM - o que você fez"
git push -u origin aula_DD-MM
```

✅ **Sempre `origin` no push. Nunca `upstream`.**

## Primeira vez: fork e clone

O fork é feito **uma vez só**.

1. Entre no GitHub e abra o [repositório da turma](https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma).
2. Clique em **Fork** > **Create fork**.
3. Confira: no topo da página deve aparecer `SEU-USUARIO / loja-turma`.
4. No terminal, rode um comando por vez, trocando `SEU-USUARIO`:

```powershell
cd $HOME\Documents
```

```powershell
git clone https://github.com/SEU-USUARIO/loja-turma.git
```

```powershell
cd loja-turma
```

```powershell
git remote add upstream https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git
```

```powershell
git remote set-url --push upstream SEM_PUSH
```

5. Abra a pasta `loja-turma` no VS Code e volte ao [passo 2](#2-confira-os-endereços).

## Problemas comuns

| O que aparece | Como resolver |
|---|---|
| `fatal: not a git repository` | O terminal está fora da pasta do projeto. Rode `cd $HOME\Documents\loja-turma`. |
| `fatal: 'upstream' does not appear to be a git repository` | O `upstream` não foi cadastrado. Rode os dois comandos do [passo 2](#2-confira-os-endereços). |
| `origin` aparece com `POO-40h-tec-web-mobile-EFG` | Você clonou o repositório da professora. Rode `git remote set-url origin https://github.com/SEU-USUARIO/loja-turma.git` e refaça o [passo 2](#2-confira-os-endereços). |
| `Permission denied`, erro `403` ou `SEM_PUSH` no `git push` | Você tentou enviar para a professora. Use sempre `git push -u origin aula_DD-MM`. |
| `fatal: a branch named 'aula_DD-MM' already exists` | A branch já existe. Entre nela com `git checkout aula_DD-MM`. |
| `error: Your local changes would be overwritten by checkout` | Você tem alterações sem commit. Rode `git add src` e `git commit -m "Aula DD-MM - salvando"`, depois repita o [passo 3](#3-crie-a-branch-da-aula). |
| Fez a atividade no `main` por engano | Rode `git checkout -b aula_DD-MM`. O seu trabalho vai junto para a branch. Depois siga o [passo 5](#5-envie-para-o-seu-repositório). |
| `nothing to commit` | Você não salvou os arquivos (`Ctrl + S`) ou já fez o commit. Rode `git status` para conferir. |
| `Author identity unknown` | Rode `git config --global user.name "Seu Nome"` e `git config --global user.email "seu-email@exemplo.com"`. |
| O `git push` pede login ou dá `Authentication failed` | Faça login no GitHub pela janela que abrir no navegador e repita o comando. |
| Abriu uma tela estranha no terminal | É o editor do Git. Digite `:q` e aperte Enter. |
| `ModuleNotFoundError: No module named 'models'` | Rode a partir da pasta `loja-turma`, não de dentro de `src`: `py src/main.py`. |
| `py` não é reconhecido | Tente `python src/main.py`. Se abrir a Microsoft Store, chame a professora. |
| O site mostra **Compare & pull request** ou **Sync fork** | Não clique em nenhum dos dois. Não é necessário. |
| Qualquer erro em vermelho que não está aqui | Não tente comandos aleatórios. Copie a mensagem e chame a professora. |

---

# VIA E-MAIL

Para quem não conseguiu usar o GitHub. **Não precisa de conta no GitHub.**

## 1. Baixe o projeto da professora

No terminal do VS Code, rode um comando por vez, trocando `DD-MM` pela data da aula:

```powershell
cd $HOME\Documents
```

```powershell
git clone https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git loja-turma-aula-DD-MM
```

*A cada aula, faça um clone novo em uma pasta com a data. Assim você sempre começa com a versão mais nova e nunca perde o que já fez.*

## 2. Abra e teste

1. No VS Code: **File** > **Open Folder** > selecione a pasta `loja-turma-aula-DD-MM`.
2. Abra o terminal: menu **Terminal** > **New Terminal**.
3. Rode o projeto:

```powershell
py src/main.py
```

## 3. Faça a atividade

Siga o roteiro da aula no `README.md` e escreva o código **somente** na pasta `src`. Rode `py src/main.py` de novo para testar.

## 4. Envie por e-mail

1. No Explorador de Arquivos, abra a pasta `loja-turma-aula-DD-MM`.
2. Clique com o botão direito na pasta `src` > **Enviar para** > **Pasta compactada**.
3. Renomeie o arquivo para `src-SEU-NOME-aula-DD-MM.zip`.
4. Envie o arquivo com estes dados:

| Campo | O que escrever |
|---|---|
| Para | `stela.edu@outlook.com` |
| Assunto | `POO - Atividade aula DD-MM - SEU NOME` |
| Anexo | `src-SEU-NOME-aula-DD-MM.zip` |

## Problemas comuns no envio por e-mail

| O que aparece | Como resolver |
|---|---|
| `git` não é reconhecido | No site da turma, clique em **Code** > **Download ZIP**, extraia e renomeie a pasta para `loja-turma-aula-DD-MM`. |
| `destination path already exists` | Você já clonou nessa pasta. Abra a pasta que já existe e continue nela. |
| O e-mail recusa o anexo | Envie o arquivo para o Google Drive, compartilhe com "qualquer pessoa com o link" e mande o link no e-mail. |
| `py` não é reconhecido | Tente `python src/main.py`. Se abrir a Microsoft Store, chame a professora. |
| `git push` dá erro `403` | No envio por e-mail não se usa `git push`. Envie só o arquivo `.zip`. |
