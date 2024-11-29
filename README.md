# Projeto de Exclusão de Emails
Este projeto visa automatizar a exclusão de emails de uma caixa de entrada de um servidor de email usando o protocolo IMAP. Ele foi desenvolvido com o objetivo de ajudar a gerenciar caixas de entrada sobrecarregadas, removendo mensagens indesejadas de forma eficiente e automatizada.

## Funcionalidades
1. Conexão com o servidor IMAP: Conecta-se a um servidor de email utilizando IMAP para acessar a caixa de entrada.
2. Exclusão de emails: Permite excluir emails de forma seletiva ou em massa com base em critérios definidos (por exemplo, idade do email, remetente, assunto) só é necessario ajustar na linha 18. Alguns possiveis filtros:
* ALL: Todas as mensagens serão apagadas
* UNSEEN: Somente as mensagens não visualizadas
* SEEN: Somente as mensagens visualizadas
* FROM: Emails enviados por um remetente específico:
* SUBJECT: Por assunto específico  

Todos os parâmetros se encontra na documentação da lib: https://docs.python.org/3/library/imaplib.html

3. Segurança: Utiliza autenticação segura (SSL/TLS) para garantir a privacidade e segurança da conexão.
4. Interface simples: O script pode ser configurado para excluir emails automaticamente sem a necessidade de interação manual.

## Tecnologias Utilizadas
* Python : Linguagem principal para desenvolvimento do script.
* imaplib: Biblioteca para comunicação com servidores IMAP.
* email: Biblioteca para manipulação de emails.

## Requisitos
Primeiro, você precisará saber o endereço do servidor IMAP do seu provedor de email. Os mais comuns são:
#### Gmail
Servidor IMAP: imap.gmail.com  
Porta: 993 

#### Outlook
Servidor IMAP: outlook.office365.com  
Porta: 993 

Também será necessário habilitar o acesso IMAP nas configurações do seu provedor de email.

## Autenticação

Você precisará fornecer seu usuário e senha de email para autenticação.
Se você estiver utilizando um serviço como o Gmail, é necessário criar uma senha de aplicativo em vez de usar a senha comum, para isso deve estar ligado a autenticação de dois fatores.

