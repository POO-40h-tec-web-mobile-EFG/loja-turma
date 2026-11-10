# Guia: como sincronizar seu fork com o repositório da turma

<https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git>&#32;

# **SIGA AS INSTRUÇÕES ABAIXO PARA SEGUIRMOS COM O PROJETO**

# VIA GITHUB

> **Regra de ouro:** você só envia (`push`) para o **seu** repositório (`origin`).
> O repositório da professora (`upstream`) é **somente leitura**: dele você só **baixa** atualizações.
>
> | Remote | De quem é | O que você faz com ele |
> |---|---|---|
> | `origin` | **Seu** fork (`SEU-USUARIO/loja-turma`) | `push` e `pull` ✅ |
> | `upstream` | Professora (`POO-40h-tec-web-mobile-EFG/loja-turma`) | só `fetch` e `merge` ⬇️ — **nunca** `push` ❌ |

---

## 1. Abrir a pasta do trabalho no VS Code

1. Abra o VS Code > **File** > **Open Folder** > selecione a pasta do projeto com o nome exato `loja-turma`, igual ao do repositório.
2. Pressione `` Ctrl + Shift + ' `` para abrir o terminal (ou use o menu **Terminal** > **New Terminal**).
3. Confira se o terminal abriu na pasta certa: o começo da linha deve terminar em `\loja-turma>`, por exemplo:

   ```
   PS C:\Users\SEU-USUARIO\Documents\loja-turma>
   ```

   - Se não abriu, vá até a pasta com o comando abaixo (o caminho muda conforme onde você salvou o projeto):

     ```powershell
     cd ~\Documents\loja-turma
     ```

4. Verifique se você fez login no GitHub no VS Code:
   - Clique no ícone de **conta** (bonequinho) no canto inferior esquerdo do VS Code.
   - Se não aparecer a sua conta do GitHub, clique em **Sign in with GitHub** e conclua o login no navegador.

5. Verifique a configuração do Git:

   ```powershell
   git config --global --list
   ```

   - Se aparecerem `user.name` e `user.email` com os dados da sua conta do GitHub, está correto.
   - Se não aparecerem, configure com o **nome de usuário** e o **e-mail** da sua conta do GitHub:

     ```powershell
     git config --global user.name "Seu Nome"
     git config --global user.email "seu-email@exemplo.com"
     ```

---

## 2. Verifique se o seu fork está configurado e atualizado

### Confira os endereços cadastrados (seu repositório e repositório da professora)

```powershell
git remote -v
```

*Lista os repositórios remotos ligados à sua pasta.*

O resultado **deve ser exatamente assim** (trocando `SEU-USUARIO` pelo seu usuário):

```
origin    https://github.com/SEU-USUARIO/loja-turma.git (fetch)
origin    https://github.com/SEU-USUARIO/loja-turma.git (push)
upstream  https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git (fetch)
upstream  SEM_PUSH (push)
```

*`origin` é o **seu** repositório. `upstream` é o repositório da **professora**.*

> ⚠️ **PARE** se aparecer `POO-40h-tec-web-mobile-EFG` na linha do `origin`. Não faça nenhum `push` e siga a seção [Corrigir `origin` errado](#corrigir-origin-errado-clonou-o-repositório-da-professora).

### Se o `upstream` não aparecer

```powershell
git remote add upstream https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git
git remote set-url --push upstream SEM_PUSH
git remote -v
```

### Se o `upstream` aparecer, mas a linha `(push)` não mostrar `SEM_PUSH`

Ative a trava que impede envio para o repositório da professora:

```powershell
git remote set-url --push upstream SEM_PUSH
git remote -v
```

*A trava bloqueia qualquer `git push upstream` (inclusive pelos botões **Sync Changes** e **Publish Branch** do VS Code). Baixar atualizações com `git fetch upstream` continua funcionando normalmente.*

### Confira se falta alguma atualização da professora

```powershell
git checkout main
git fetch upstream
git log --oneline main..upstream/main
```

- **`git checkout main`** — garante que você está na branch `main` do seu projeto.
- **`git fetch upstream`** — baixa as atualizações do repositório da professora para o seu computador, sem mexer nos seus arquivos nem no seu `main`.
- **`git log --oneline main..upstream/main`** — lista os commits que estão no `main` da professora e ainda não estão no seu `main`, um por linha. Só mostra, não altera nada.

Resultado:

- **Sem nenhuma saída:** o seu `main` já tem tudo da professora ✅. Vá para o [passo 4](#4-crie-uma-branch-da-aula).
- **Se listar commits:** são atualizações que faltam. Siga o [passo 3](#3-atualize-seu-repositório-com-a-atividade-de-hoje).

---

### Se você ainda não fez o fork nas aulas anteriores

> O fork é feito **apenas uma vez**. Se você já fez, pule esta etapa.

1. Faça login na sua conta do GitHub pelo navegador e abra o repositório da turma: [POO-40h-tec-web-mobile-EFG/loja-turma](https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma).
2. Clique em **Fork** (canto superior direito). Mantenha o nome `loja-turma`, deixe marcado **Copy the main branch only** e clique em **Create fork**.
   - Confira: no topo deve aparecer `SEU-USUARIO / loja-turma` e, logo abaixo, *forked from POO-40h-tec-web-mobile-EFG/loja-turma*.
3. No **seu** fork, clique em **Code** e copie o endereço HTTPS.
4. No terminal, vá até a pasta onde você guarda seus projetos e rode:

   ```powershell
   cd ~\Documents
   git clone https://github.com/SEU-USUARIO/loja-turma.git
   cd loja-turma
   git remote add upstream https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git
   git remote set-url --push upstream SEM_PUSH
   git remote -v
   ```

5. O `git remote -v` deve mostrar o resultado igual ao [modelo acima](#confira-os-endereços-cadastrados-seu-repositório-e-repositório-da-professora). Depois, abra a pasta `loja-turma` no VS Code ([passo 1](#1-abrir-a-pasta-do-trabalho-no-vs-code)).

> ⚠️ **Atenção:** clone o **seu** fork, **não** o repositório da professora.

### Corrigir `origin` errado (clonou o repositório da professora)

Se o `origin` aparecer com `POO-40h-tec-web-mobile-EFG`, rode **todos** os comandos abaixo, na ordem:

```powershell
git remote rename origin upstream
git remote add origin https://github.com/SEU-USUARIO/loja-turma.git
git fetch origin
git branch -u origin/main main
git remote set-url --push upstream SEM_PUSH
git remote -v
git branch -vv
```

- **`git remote rename origin upstream`** — o endereço da professora passa a se chamar `upstream`.
- **`git remote add origin ...`** — cadastra o **seu** fork como `origin`.
- **`git fetch origin`** — baixa as informações do seu fork.
- **`git branch -u origin/main main`** — liga o seu `main` ao **seu** fork. *Sem este comando, o `main` continuaria ligado ao repositório da professora.*
- **`git remote set-url --push upstream SEM_PUSH`** — ativa a trava contra push na professora.

Confira:

- `git remote -v` deve ficar igual ao [modelo](#confira-os-endereços-cadastrados-seu-repositório-e-repositório-da-professora).
- `git branch -vv` deve mostrar o `main` com **`[origin/main]`**. Se aparecer `[upstream/main]`, repita o comando `git branch -u origin/main main`.

---

## 3. Atualize seu repositório com a atividade de hoje

### Traga as atualizações da professora

```powershell
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

*Se não aparecer `CONFLICT`, deu certo. Pule para o [passo 4](#4-crie-uma-branch-da-aula).*

### Se aparecer `CONFLICT`

Isso acontece quando você fez commit direto no `main`. Primeiro cancele o merge e guarde o seu trabalho numa branch de backup:

```powershell
git merge --abort
git branch meu-trabalho
git push origin meu-trabalho
```

Depois deixe o seu `main` igual ao da professora:

```powershell
git merge upstream/main -X theirs -m "Sincroniza com a turma"
git restore --source=upstream/main --staged --worktree -- .
git commit -m "Garante versão da professora"
git push origin main
```

*Se aparecer `nothing to commit`, já está igual e o `push` resolve. O seu código antigo continua salvo na branch `meu-trabalho`.*

### Confira

```powershell
git diff --stat upstream/main
```

*Se não mostrar nada, o seu `main` está igual ao da professora.*

---

## 4. Crie uma branch da aula

```powershell
git checkout -b aula_DD-MM
```

*Troque `DD-MM` pela data de hoje. Exemplo para 10 de novembro: `git checkout -b aula_10-11`.*
*Faça o exercício **nesta branch**, nunca no `main`.*

### Confira se você está na branch da aula

1. Olhe o **canto inferior esquerdo** do VS Code: deve aparecer o nome `aula_DD-MM` ao lado do ícone de branch.
2. Ou rode no terminal:

   ```powershell
   git status
   ```

   A primeira linha deve dizer `On branch aula_DD-MM`.

3. Se aparecer `On branch main`, troque para a branch da aula (sem `-b`, porque ela já existe):

   ```powershell
   git checkout aula_DD-MM
   ```

*O `-b` só é usado na primeira vez, para **criar** a branch. Confira a branch sempre antes de fazer `git commit`.*

### Ao terminar o exercício, salve no seu repositório

```powershell
git add .
git commit -m "Exercício aula DD-MM"
git branch -vv
git push -u origin aula_DD-MM
```

Antes do `push`, confira a saída do `git branch -vv`:

- A branch atual (marcada com `*`) **não pode** mostrar `[upstream/...]`.
- Na primeira vez, é normal a branch da aula aparecer **sem nada** entre colchetes. Depois do `push`, ela passa a mostrar `[origin/aula_DD-MM]`.

> 💡 **O `-u` não tem nada a ver com o `upstream` da professora.**
> `-u` é a forma curta de `--set-upstream`: ele apenas liga a sua branch local à branch de mesmo nome no **seu** `origin`. Depois disso, um simples `git push` já sabe para onde enviar.
> Quem decide o destino é a palavra **`origin`** no comando.

> 💡 **Usando os botões do VS Code?** Se o VS Code perguntar para qual remote publicar (**Publish Branch**), escolha sempre **`origin`**.

---

## 5. Veja as orientações da aula de hoje

As orientações ficam na pasta `_Orientacoes_e_apoio`, no arquivo com a data da aula, por exemplo:

```
loja-turma\_Orientacoes_e_apoio\Aula 10-11-2026.md
```

1. No VS Code, abra a pasta `_Orientacoes_e_apoio` (na raiz do projeto, fora da pasta `src`) e clique no arquivo da aula de hoje.
2. Pressione `Ctrl + Shift + V` para ver o arquivo `.md` formatado, com títulos, imagens e tabelas. Se preferir, abra o arquivo pelo repositório da turma no navegador.
3. Veja o diagrama e as regras e construa de acordo com cada um:
   - Crie **cada classe em um arquivo** `.py` dentro da pasta `src/models/` (exemplo: `src/models/cliente.py`).
   - Depois, teste as implementações no arquivo `src/main.py`.
4. Depois de cada bloco, rode o projeto para testar:

   ```powershell
   python src/main.py
   ```

> ⚠️ **Não edite o `README.md` nem os arquivos de `_Orientacoes_e_apoio`**: eles são da professora, e alterações neles causam conflito na próxima atualização. Para fazer anotações, crie o seu próprio arquivo, por exemplo `minhas_anotacoes.md`.

---

## Resumo rápido (cola de bolso)

```powershell
# 1. Conferir remotes (origin = SEU usuário | upstream push = SEM_PUSH)
git remote -v

# 2. Atualizar o main com a professora
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 3. Criar a branch da aula
git checkout -b aula_DD-MM

# 4. Ao terminar
git add .
git commit -m "Exercício aula DD-MM"
git branch -vv
git push -u origin aula_DD-MM
```

✅ **Sempre `origin` no push. Nunca `upstream`.**

## **- Cuidados:**

- Nunca clique em **Open pull request** nem em **Discard commits** no aviso do Sync fork no GitHub.
- O `git commit -m` precisa de uma mensagem entre aspas: `git commit -m ""` dá erro.
- Se o `git merge` disser `would be overwritten by merge`, você tem alterações sem commit: rode `git add .` e `git commit -m "mensagem"` e repita o passo 3.
- Cole no terminal só os comandos, nunca outro texto.
- Outros problemas comuns e como resolver: veja a tabela abaixo.

### **- Problemas comuns:**

| Mensagem ou situação | Como resolver |
| --- | --- |
| `fatal: not a git repository` | O terminal está fora da pasta do projeto. Volte para ela com `cd` (passo 1). |
| `fatal: 'upstream' does not appear to be a git repository` | O upstream não foi cadastrado. Rode o `git remote add upstream ...` do passo 2. |
| `Permission denied` ou erro 403 no `git push` | Você está tentando enviar para o repositório da professora. Confira com `git remote -v`: o `origin` tem que ser o **seu** usuário. |
| O `git push` pede login ou dá `Authentication failed` | Faça login no GitHub pela janela que abrir no navegador e repita o comando. |
| `error: pathspec 'aula-10-11' did not match` | A branch ainda não existe. Crie com `git checkout -b aula-10-11`. |
| `fatal: a branch named 'aula-10-11' already exists` | A branch já foi criada. Só troque para ela com `git checkout aula-10-11`. |
| Abriu uma tela estranha no terminal depois do `git merge` ou do `git commit` | É o editor de texto do Git (Vim). Digite `:wq` e aperte Enter para salvar e sair. |
| `ModuleNotFoundError` ao rodar o projeto | Rode a partir da pasta `loja-turma` (não de dentro de `src`): `python src/main.py`. |
| Fez o exercício e o commit no `main` por engano | Rode `git checkout -b aula-10-11` para levar o trabalho para a branch da aula. Na próxima atualização, se der `CONFLICT`, siga o passo 3. |
| Qualquer erro em vermelho que não está aqui | Não tente comandos aleatórios. Copie a mensagem e chame a professora. |
| `python` não é reconhecido, ou abre a Microsoft Store | chame a professora |

# **VIA EMAIL****:**

**Para quem não está acompanhando pelo GitHub. Não precisa de conta nem de comandos Git.**

## **1. Baixe o projeto da professora**

1. Abra o repositório da turma: [https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma](https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma).
2. Clique no botão verde **Code** e depois em **Download ZIP**.
3. Na pasta Downloads, clique com o botão direito no arquivo `loja-turma-main.zip` e escolha **Extrair tudo**.
4. Renomeie a pasta extraída de `loja-turma-main` para `loja-turma` e mova para a sua pasta de projetos (ex.: `C:\DOCUMENTOS\`).

*Se você já tem uma pasta `loja-turma` de aulas anteriores, não substitua: renomeie a antiga para `loja-turma-antigo` antes, para não perder o seu código.*

## **2. Abra e rode no seu computador**

1. Abra o VS Code > **File** > **Open Folder** e selecione a pasta `loja-turma`.
2. Abra o terminal (`Ctrl + Shift + '` ou menu **Terminal** > **New Terminal**).
3. Rode o projeto:

```powershell
python src/main.py
```

*Se aparecer erro de `import`, chame a professora antes de mexer no código.*

## **3. Faça a atividade**

Siga as orientações da aula no `aula_10-11.md` e faça o exercício nos arquivos da pasta `src`. Rode `python src/main.py` de novo para testar.

## **4. Envie por e-mail**

1. Clique com o botão direito na pasta `loja-turma` > **Enviar para** > **Pasta compactada (zipada)**.
2. Renomeie o arquivo para `loja-turma-SEU-NOME-aula-10-11.zip` (troque pela data da aula).
3. Envie para o e-mail da professora ` stela.edu@outlook.com` com o assunto: ` POO - Atividade aula  10-11 - SEU NOME`.

*Se o e-mail recusar o anexo, envie pelo Google Drive e mande o link no e-mail, coloque compartilhamento público para que professora possa baixar e visualizar**.*
