import imaplib
import email


imap_servidor = 'imap.gmail.com'
imap_porta = 993
login = 'seu_login'
senha = 'sua_senha'

try:
    mail = imaplib.IMAP4_SSL(imap_servidor, imap_porta)
    mail.login(login, senha)
    print('Conexão bem sucedida')
    
    mail.select("inbox")
    print('Entrou no inbox')

    status, messages = mail.search(None, 'ALL')
    print(status)

    for message_id in messages[0].split():
        # Extrair a mensagem
        status, msg_dados = mail.fetch(message_id, "(RFC822)")
        email_lido = msg_dados[0][1]
        msg = email.message_from_bytes(email_lido)
        remetente = msg['From']
         
        # Apagar tudo  
        mail.store(message_id, '+FLAGS', '\\Deleted')
        print(f'Mensagem de {remetente} apagada.')

    mail.expunge()
    mail.close()
    mail.logout() 
except Exception as e:
    print(f'Erro ao conectar ao servidor IMAP: {e}')