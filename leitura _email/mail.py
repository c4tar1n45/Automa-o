#envio para multiplos destinatários
#conteúdo do e-mail em formato HTML, para incluir formatação de textos e links.

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'botsilva410@gmail.com'
senha = 'yrlo ojjo iwyc srkk'
copia = 'copia@example.com'

try:
    print('Aguarde...seu e-mail está sendo enviado!')
    #Configurações do servidor de e-mail
    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()
    #servidor_email.login('Seu_email', 'Sua senha')
    servidor_email.login(email, senha)

    #Montar o email
    remetente = email
    destinatário = [email]
    copia = [copia]
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = ', '.join(destinatário)
    mensagem['Cc'] = ', '.join(copia)
    #Título do email
    mensagem['Subject'] = 'Teste de envio para e-mails em cópia'
    #conteúdo do email
    corpo_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
            body { font-family: Arial, sans-serif; color: #333; }
            .card { border: 1px solid #ddd; padding: 16px; border-radius: 8px; max-width: 500px; }
            .header { color: #2b5797; font-size: 18px; font-weight: bold; }
            .highlight { background-color: #e7f3fe; border-left: 4px solid #2196F3; padding: 8px; margin: 12px 0; }
            .footer { font-size: 12px; color: #777; margin-top: 16px; }
            </style>
        </head>
        <body>
            <div class="card">
            <div class="header">Notificação Automática</div>
            <p>Olá,</p>
            <p>Este e-mail foi gerado e formatado via script <strong>Python</strong>.</p>
            
            <div class="highlight">
                <strong>Status:</strong> Processo concluído com sucesso!
            </div>

            <p class="footer">E-mail automático. Por favor, não responda diretamente a esta mensagem.</p>
            </div>
        </body>
        </html>
        """

    mensagem.attach(MIMEText(corpo_html, 'html', 'utf-8'))

    #Envio do e-mail
    servidor_email.sendmail(remetente, destinatário, mensagem.as_string())

    print('E-mail enviado com sucesso!')

except Exception as e:
    print('Erro ao enviar e-mail: {e}')
