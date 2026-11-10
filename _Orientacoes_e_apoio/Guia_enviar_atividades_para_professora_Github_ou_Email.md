# Guia: como sincronizar seu fork com o repositório da turma

<https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git>&#32;

# **SIGA AS INSTRUÇÕES ABAIXO PARA SEGUIRMOS COM O PROJETO**

# **VIA GITHUB:**

## **1. Abrir pasta do trabalho no VS Code**

##### 1. Abra o VS Code > File > Open folder > Selecione a pasta do projeto com nome exato "loja-turma" igual ao do repositório.
##### 2. Pressione ` Ctrl + Shift + ' ` para abrir o terminal (ou use o menu Terminal > New Terminal)
##### 3. Confira se o terminal abriu na pasta certa: o começo da linha deve terminar em `\loja-turma>`, por exemplo `PS C:\Users\SEU-USUARIO\DOCUMENTOS\loja-turma>`.
   1. Se não abriu, vá até a pasta com o comando `cd C:\Users\SEU-USUARIO\DOCUMENTOS\loja-turma` (ou o atalho `cd ~\DOCUMENTOS\loja-turma`). O caminho muda conforme onde você salvou o projeto.
##### 4. Cheque se você fez o login no github no VS Code
   1. Caso não tenha feito login, faça pelo navegador&#91;image: image.png\]&#91;image: image.png\]
##### 5. Verifique como está a configuração do git:&#32;

   ```
   git config --global --list
   ```
   1. Se aparecerem `user.name` e `user.email` com o seu usuário do github, está correto.&#32;
6. Se não aparecerem, configure com:\
• nome de usuário da sua conta do GitHub.\
• e-mail da sua conta do GitHub.

   ```
   git config --global user.name "Seu Nome" 
   git config --global user.email "seu-email@exemplo.com" 
   ```

## **2. Verifique se você está com o fork atualizado**

### **Confira se os dois endereços estão cadastrados (seu repositorio e repositorio professora):**

```powershell
git remote -v
```

*comando para listar os repositórios remotos ligados à sua pasta*

Devem aparecer:

![alt text](imagens/image.png)

***origin **é o seu repositorio, **upstream **é o repositório professora.*

### **- ****Se o `upstream` não aparecer, rode: **

```
git remote add upstream ...
```

Depois, confira se falta alguma atualização do professor:

```powershell
git checkout main
git fetch upstream
git log --oneline main..upstream/main
```

***git checkout main**** **-***** *garante que você está na branch main do seu projeto*\
***git fetch upstream**** -*** ***baixa as atualizações do repositório da professora (upstream) para o seu computador, sem mexer nos seus arquivos nem no seu main. \
**git log --oneline main..upstream/main**** -***** *lista os commits que estão no main da professora e ainda não estão no seu main, um por linha. Ele só mostra, não altera nada.*

- **Sem nenhuma saída:** o seu `main` já tem tudo do professor ✅. Vá para o passo 4
- **Se listar commits:** são atualizações que faltam. Siga o passo 3 (Atualize seu repositório com a atividade de hoje).

### **-** **Se não estiver feito fork nas aulas anteriores:**

Fork deve ser feito apenas uma vez, só faça fork se você não tiver feito no início. Se já tiver feito o fork, pule esta etapa.

1. Faça o login na sua conta do GitHub pelo navegador e abra o repositório da turma: [POO-40h-tec-web-mobile-EFG/loja-turma](https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma).
2. Clique em **Fork** (canto superior direito). Mantenha o nome `loja-turma`, deixe marcado *Copy the main branch only* e clique em **Create fork**.
   1. Confira: no topo deve aparecer `SEU-USUARIO / loja-turma` e, logo abaixo, *forked from POO-40h-tec-web-mobile-EFG/loja-turma*.
3. No seu fork, clique em **Code** e copie o endereço HTTPS.
4. No terminal, vá até a pasta onde você guarda seus projetos (ex.: `cd ~\DEV`) e rode:

```powershell
git clone https://github.com/SEU-USUARIO/loja-turma.git
cd loja-turma
git remote add upstream https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma.git
git remote -v
```

O `git remote -v` deve mostrar `origin` com o **seu** usuário e `upstream` com `POO-40h-tec-web-mobile-EFG`. Depois, abra a pasta `loja-turma` no VS Code (passo 1).

**Atenção:** clone o **seu** fork, não o repositório do professor. Se o `origin` aparecer com `POO-40h-tec-web-mobile-EFG`, corrija assim:

```powershell
git remote rename origin upstream
git remote add origin https://github.com/SEU-USUARIO/loja-turma.git
git remote -v
```

## **3. Atualize seu repositório com a atividade de hoje**

### **- Traga as atualizações da professora:**

```powershell
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

*Se não aparecer `CONFLICT`, deu certo. Pule para o passo 4.*

### **- Se aparecer `CONFLICT`:**

Isso acontece quando você fez commit no `main`. Primeiro cancele o merge e guarde o seu trabalho numa branch de backup:

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

### **- Confira:**

```powershell
git diff --stat upstream/main
```

*Se não mostrar nada, o seu `main` está igual ao da professora.*

## **4. Crie uma** **branch da aula**

```
git checkout -b aula-05-11
```

*Troque `0``5`**`-11` pela data de hoje. Faça o exercício nesta branch, nunca no `main`.*

### **- Verifique se está trabalhando na branch criada****:**

### **- Confira se você está na branch criada para ****a aula:**

1. Olhe o **canto inferior esquerdo** do VS Code: deve aparecer o nome `aula-0``5``-11` ao lado do ícone de branch.
2. Ou rode no terminal:

```powershell
git status
```

A primeira linha deve dizer `On branch aula-0``5``-11`.

3. Se aparecer `On branch main`, troque para a branch da aula (sem `-b`, porque ela já existe):

```
git checkout aula-05-11
```

*O `-b` só é usado na primeira vez, para criar a branch. Confira a branch sempre antes de fazer `git commit`.*

### **- Ao terminar o exercício, salve no seu repositório:**

```
git add .
git commit -m "Exercício aula 05-11"
git push -u origin aula-05-11
```

## **5****. Veja as orientações da aula de hoje em loja-turma\\\_****Orientacoes*\_*e\_apoio\\aula\_10-11****.md**** **

1. No VS Code, clique no arquivo `aula_10-11.md` (na raiz do projeto, fora da pasta `src`).
2. Pressione `Ctrl + Shift + V` no vs copara ver o arquivo .md formatado, com títulos e tabelas. Se preferir, abra o repositório da turma no navegador: o README aparece logo abaixo da lista de arquivos.
3. Veja o diagrama e as regras, construa de acordo com cada um. Crie cada classe em um arquivo.py dentro da pasta `src/models/classe.py`. depois teste as implementações no arquivo `main.py`.
4. Depois de cada bloco, rode o projeto para testar:

```powershell
python src/main.py
```

*Não edite o `README.md`: ele é da professora e alterações nele causam conflito na próxima atualização. Para fazer anotações, crie o seu próprio arquivo, por exemplo `minhas_anotacoes.md`.*

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

***Para quem não ******e**stá **a**comp**anhando****** **pelo****** ******GitHub. Não precisa de conta nem de comandos Git.***

## **1. Baixe o projeto da professora**

1. Abra o repositório da turma: [https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma](https://github.com/POO-40h-tec-web-mobile-EFG/loja-turma).
2. Clique no botão verde **Code** e depois em **Download ZIP**.
3. Na pasta Downloads, clique com o botão direito no arquivo `loja-turma-main.zip` e escolha **Extrair tudo**.
4. Renomeie a pasta extraída de `loja-turma-main` para `loja-turma` e mova para a sua pasta de projetos (ex.: `C:\``D``OCU``MEN``TOS``\`).

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
2. Renomeie o arquivo para `loja-turma-SEU-NOME-aula-``1``0``-11.zip` (troque pela data da aula).
3. Envie para o e-mail da professora com o assunto: ` POO - Atividade aula  ``1``0``-11 - SEU NOME`.

*Se o e-mail recusar o anexo, envie pelo Google Drive e mande o link no e-mail, coloque compartilhamento público para que professora possa baixar e visualizar**.*
