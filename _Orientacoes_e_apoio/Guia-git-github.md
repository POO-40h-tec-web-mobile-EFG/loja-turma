# Git e GitHub no laboratório: como trabalhar com segurança

Os computadores do laboratório são de uso coletivo. Hoje você está nesta máquina; amanhã, outra turma senta no mesmo lugar. Se a sua conta do GitHub ficar aberta, quem vier depois pode enviar código no seu nome, mexer no seu repositório ou até apagá-lo.

Por isso, a combinação da turma é simples: **quem entra, sai**. Toda aula começa com o login e termina com o logout. Leva só cinco minutos e evita muita dor de cabeça.

Este guia mostra o caminho completo, do momento em que você liga o computador até a hora de ir embora. Se algum termo for novo para você (commit, clone, branch...), dê uma olhada no [glossário](#7-glossário) no fim do guia.

---

## O que é GIT?
Git é um sistema de controle de versão: registra cada alteração do código, permite voltar a versões anteriores e trabalhar em equipe sem um sobrescrever o trabalho do outro.


## O que é GITHUB? 
GitHub é uma plataforma online que guarda repositórios Git na nuvem. Nela você compartilha código, colabora com outras pessoas e monta um portfólio dos seus projetos.


SAIBA MAIS: https://www.youtube.com/watch?v=-l4Aa8wef8s

---

## 1. Combinados da turma

| Combinado | Por quê |
|---|---|
| Não salvar a senha no navegador | A próxima pessoa entraria na sua conta sem digitar nada. |
| Não usar a conta de colega nem emprestar a sua | O histórico do projeto mostra quem fez cada alteração. Ele precisa ser verdadeiro. |
| Conferir de quem é a conta antes de enviar | Evita mandar o seu código para o repositório errado. |
| Fazer o logout completo, mesmo com pressa | É o único jeito de garantir que ninguém usa a sua conta depois. |
| Ativar a verificação em duas etapas (2FA) | Mesmo que alguém descubra a sua senha, não consegue entrar sem o código do seu celular. |

---

## 2. Chegando na aula: login

### 2.1 Veja se a máquina está limpa

Abra o VS Code e, no menu de cima, clique em **Terminal** → **Novo Terminal**. Um terminal (PowerShell) vai abrir na parte de baixo da tela. Digite:

```powershell
git config --global --list
```

Se aparecer o nome ou o e-mail de outra pessoa, alguém esqueceu de sair. Chame a professora antes de continuar.

Depois, faça mais duas conferências:

| Onde olhar | Como chegar lá | O que fazer se tiver conta de outra pessoa |
|---|---|---|
| Contas do VS Code | Ícone de **Contas**, o bonequinho no canto inferior esquerdo | Clicar na conta e escolher **Sair** (*Sign Out*). |
| Gerenciador de Credenciais do Windows | Tecla **Windows** → digite **Gerenciador de Credenciais** → **Credenciais do Windows** | Procurar um item chamado `git:https://github.com`, clicar nele e depois em **Remover**. |

### 2.2 Diga ao Git quem você é

Use o mesmo e-mail da sua conta do GitHub:

```powershell
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email@exemplo.com"
```

### 2.3 Abra o seu projeto

Cada aluno trabalha na **sua própria cópia** do projeto, chamada **fork**: `github.com/SEU-USUARIO/loja-turma`.

| Situação | O que fazer |
|---|---|
| **Primeira aula:** você ainda não tem o fork | Abra `github.com/POO-40h-tec-web-mobile-EFG/loja-turma`, clique em **Fork** → **Create fork**. Confira se o endereço virou `github.com/SEU-USUARIO/loja-turma`. |
| **Toda aula:** trazer as novidades do repositório da turma | No site, abra o **seu fork** e clique em **Sync fork** → **Update branch**. |
| A pasta do projeto **não** está na máquina | No terminal: `cd $HOME\Documents`, depois `git clone https://github.com/SEU-USUARIO/loja-turma.git`, `cd loja-turma` e `code .` (troque `SEU-USUARIO` pelo seu usuário). |
| A pasta **já** está na máquina | Abra a pasta no VS Code e rode `git pull` no terminal (ou clique em **Sincronizar Alterações**). |

> ⚠️ Clone sempre o **seu fork**, nunca o `loja-turma` da organização. Se clonar o da organização, o envio vai dar erro de permissão.

### 2.4 Conecte o VS Code ao GitHub

Na primeira vez que você enviar algo, vai aparecer um pedido para entrar com o GitHub. No Windows, ele pode vir de dois jeitos:

| O que aparece | O que fazer |
|---|---|
| Aviso do VS Code pedindo para entrar com o GitHub | Clique em **Permitir**, faça login no navegador e confirme em **Authorize Visual-Studio-Code**. |
| Janela **Connect to GitHub** (do Git Credential Manager) | Clique em **Sign in with your browser**, faça login no navegador e confirme em **Authorize**. |

Depois é só voltar para o VS Code. Nos dois casos, o Windows guarda o acesso no Gerenciador de Credenciais, e é por isso que ele precisa ser limpo no fim da aula.

Se o navegador (Edge ou Chrome) oferecer para guardar a senha, a resposta é sempre **"Nunca"**. Também não entre com a sua conta da Microsoft ou do Google no navegador da escola.

---

## 3. Durante a aula: salvando o trabalho no GitHub

Repita este ciclo sempre que terminar uma parte do exercício:

| Passo | Onde | O que fazer |
|---|---|---|
| 1 | Editor | Salve os arquivos com `Ctrl + S`. |
| 2 | Barra lateral | Abra o **Controle do Código-Fonte** (*Source Control*). |
| 3 | Caixa de mensagem | Escreva o número da aula e o que você fez, por exemplo: `Aula 3 - cria classe Produto`. |
| 4 | Botão **Commit** | Clique. Se ele perguntar sobre preparar (*stage*) as alterações, responda **Sim**. |
| 5 | Botão **Sincronizar Alterações** | Clique para enviar ao GitHub. |
| 6 | Site do GitHub | Atualize a página do **seu fork** e confira se a alteração chegou. |

Pelo terminal, o mesmo ciclo é:

```powershell
git add .
git commit -m "Aula 3 - cria classe Produto"
git push
```

Vale a pena fazer commits pequenos ao longo da aula, em vez de um só no final. Se o computador travar, o que já foi enviado está seguro.

---

## 4. Indo embora: logout

Este é o momento mais importante. Atente-se se você realizou os passos abaixo antes de ir embora:

- [ ] Fiz o último commit e conferi no site do GitHub que está tudo lá.
- [ ] Saí da conta no VS Code: **Contas** → minha conta do GitHub → **Sair**.
- [ ] Limpei o meu nome e e-mail do Git, com os comandos da tabela abaixo.
- [ ] Apaguei o acesso guardado pelo Windows (veja "Gerenciador de Credenciais" abaixo).
- [ ] Saí do GitHub no navegador: foto no canto superior direito → **Sign out**.
- [ ] Fechei todas as janelas do navegador, do VS Code e do terminal.
- [ ] Se a professora pediu, apaguei a pasta do projeto e esvaziei a **Lixeira**. O código continua guardado no GitHub.

### Comandos de limpeza

No terminal do VS Code (**Terminal** → **Novo Terminal**):

| Comando | O que ele faz |
|---|---|
| `git config --global --unset user.name` | Apaga o seu nome do Git. |
| `git config --global --unset user.email` | Apaga o seu e-mail do Git. |
| `cmdkey /delete:git:https://github.com` | Apaga o acesso ao GitHub que o Windows guardou. |
| `git config --global --list` | Mostra o que sobrou. O seu nome e o seu e-mail não podem aparecer. |

Se algum comando responder que não encontrou nada, está tudo certo: quer dizer que já estava limpo.

### Gerenciador de Credenciais

Se preferir fazer pela tela, ou para conferir se o comando `cmdkey` funcionou:

1. Aperte a tecla **Windows** e digite **Gerenciador de Credenciais**.
2. Clique em **Credenciais do Windows**.
3. Procure itens com **github** no nome, como `git:https://github.com`.
4. Clique em cada um e depois em **Remover**.

Se não houver nenhum item com github no nome, está tudo certo.

---

## 5. Esqueci de sair. E agora?

Calma, dá para resolver de qualquer computador ou pelo celular:

1. Entre em github.com e vá em **Settings** → **Applications** → aba **Authorized OAuth Apps**.
2. Clique em **Visual Studio Code** e depois em **Revoke**. Se aparecer também **Git Credential Manager**, faça o mesmo com ele. Isso desconecta todas as máquinas de uma vez.
3. Em **Settings** → **Sessions**, encerre as sessões que você não reconhece.
4. Se acha que alguém viu a sua senha, troque a senha.
5. Avise a professora na próxima aula.

---

## 6. Deu erro? Veja se é um destes

| Mensagem ou situação | O que costuma ser | Como resolver |
|---|---|---|
| *Author identity unknown* ou *Please tell me who you are* | O Git não sabe quem você é. | Refaça a seção 2.2. |
| O VS Code mostra o nome de outra pessoa em Contas | Alguém não fez o logout. | Clique em **Sair** na conta dela, entre com a sua e avise a professora. |
| *Permission denied* ou erro 403 no envio | O Windows ainda guarda o acesso de outra pessoa. | Remova o item `git:https://github.com` no **Gerenciador de Credenciais** (seção 4) e envie de novo. Vai aparecer o pedido para entrar com a sua conta. |
| O envio foi sem pedir login, mesmo depois de sair do VS Code | O acesso ficou guardado no Gerenciador de Credenciais. | Remova o item `git:https://github.com` (seção 4). |
| `git` não é reconhecido como comando | O Git não está instalado na máquina, ou o VS Code foi aberto antes da instalação. | Feche e abra o VS Code. Se continuar, avise a professora. |
| *Permission denied* ou 403 mesmo depois de limpar a credencial | Você clonou o `loja-turma` da organização, não o seu fork. | Copie a pasta `src` para outro lugar, clone o **seu fork** (seção 2.3), cole a `src` de volta e envie de novo. |
| **Sync fork** avisa conflito | Você alterou um arquivo que a professora também alterou. | Chame a professora. |
| *rejected* ou *fetch first* no envio | O GitHub tem alterações que ainda não estão na sua máquina. | Rode `git pull` (ou clique em **Sincronizar Alterações**) e envie de novo. |
| O navegador quer salvar a senha | Ele faz isso por padrão. | Responda **"Nunca"** ou **"Agora não"**. |

---

## 7. Glossário

Estes são alguns termos que vamos usar muito durante o curso. Ter o significado sempre à mão ajuda a fixar o conteúdo e a se acostumar com os conceitos. Não precisa decorar: volte aqui sempre que um deles aparecer.

Os termos foram adaptados do [Glossário do Curso Fundamentos do GitHub](https://aline-antunes.gitbook.io/formacao-fundamentos-github), de Aline Antunes.

### Git

| # | Termo | O que significa |
|---|---|---|
| 1 | **Branch** (ramificação) | Uma linha de desenvolvimento independente. Permite trabalhar em um recurso novo ou corrigir um bug sem afetar o código principal. |
| 2 | **Merge** (mesclar) | Juntar as alterações de uma branch em outra. |
| 3 | **Rebase** | Reorganizar o histórico de commits, geralmente para deixá-lo mais limpo e em linha reta. |
| 4 | **Clone** | Criar uma cópia local, no seu computador, de um repositório remoto. |
| 5 | **Fork** | Criar uma cópia pessoal do repositório de outra pessoa, para contribuir com ele ou desenvolver por conta própria. |
| 6 | **Commit** | Um conjunto de mudanças relacionadas, registrado no histórico do repositório. |
| 7 | **Pull Request** (pedido de pull) | Um pedido para incorporar as alterações de uma branch (muitas vezes vinda de um fork) em outra. |
| 8 | **Remote** (remoto) | Repositório que fica em outro lugar. No nosso caso, quase sempre é o repositório no GitHub. |
| 9 | **Tag** | Uma marcação em um commit específico, normalmente usada para identificar versões estáveis. |
| 10 | **Stash** | Guardar alterações temporariamente, para trocar de branch sem precisar fazer commit nem descartar o que foi feito. |

### GitHub

| # | Termo | O que significa |
|---|---|---|
| 1 | **Issues** (problemas) | Onde se registram e acompanham tarefas, melhorias ou bugs de um repositório. |
| 2 | **Wiki** | Páginas de documentação ligadas a um repositório. |
| 3 | **Actions** | Automações configuradas no GitHub para executar tarefas, testes ou implantações. |
| 4 | **GitHub Pages** | Serviço que publica um site direto a partir do seu repositório. |
| 5 | **Collaborator** (colaborador) | Pessoa que tem permissão para contribuir diretamente em um repositório. |
| 6 | **Organization** (organização) | Uma conta do GitHub que reúne vários repositórios e membros, como a organização da nossa turma. |
| 7 | **Gist** | Um repositório Git mínimo, usado para compartilhar pequenos trechos de código. |
| 8 | **Code Review** (revisão de código) | Avaliação do código por outras pessoas da equipe, para melhorar a qualidade e encontrar possíveis problemas. |
| 9 | **Dependency** (dependência) | Uma biblioteca ou pacote de que o seu projeto precisa para funcionar. |
| 10 | **Contributing Guidelines** (diretrizes de contribuição) | Instruções sobre como contribuir com um projeto específico. |

---

## Para saber mais

- [Glossário do Curso Fundamentos do GitHub](https://aline-antunes.gitbook.io/formacao-fundamentos-github), de Aline Antunes: termos do Git (branch, commit, clone, merge...) e do GitHub (issues, pull request, organization...) explicados de forma simples.
- [Documentação oficial do Git: git config](https://git-scm.com/docs/git-config)
- [Git Credential Manager: como o Windows guarda o acesso ao GitHub](https://github.com/git-ecosystem/git-credential-manager)
- [Documentação do VS Code: contas e login com GitHub](https://code.visualstudio.com/docs/setup/copilot)
