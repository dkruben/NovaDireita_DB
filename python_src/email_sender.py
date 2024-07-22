# -*- coding: utf-8 -*-
import os
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


class EmailSender:
    def __init__(self):
        self.sender_mail = os.getenv('SENDER_EMAIL', 'tomar@novadireita.pt')
        self.password = os.getenv('EMAIL_PASSWORD', 'BQr{E]2pmLU(')
        self.smtp_server = os.getenv('SMTP_SERVER', 'mail.novadireita.pt')
        self.smtp_port = int(os.getenv('SMTP_PORT', 465))
    
    def send_email(self, to, name):
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Nova Direita - Inscrição'
        message['From'] = formataddr(('Nova Direita', self.sender_mail))
        message['To'] = to
        message['Importance'] = 'high'
        
        html = f"""
        <!DOCTYPE html>
        <html lang='pt'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>(no-reply) - Nova Direita</title>
        </head>
        <body>
        <div>
            <h2>Saudações, sr.(a) {name}!</h2>
            <h3>
                Em nome de toda a equipe do Nova Direita, é com grande prazer que confirmo a aceitação de sua filiação como membro activo de nosso Partido Político<br><br>
                A sua decisão de se juntar a nós, é o testemunho do seu compromisso com os valores e objectivos que defendemos e implica a aceitação dos estatutos e declaração de princípios, aprovados no Congresso Fundador e que se encontram em anexo.<br>
                Para começar a sua jornada connosco, gostaria de convidá-lo a efectuar o pagamento da sua quota anual de membro, no valor de 30€, para o IBAN do<br>
                partido que se encontra em anexo. De seguida, envie o comprovativo para o email<br>
                <a href="mailto:secretariageral@novadireita.pt">secretariageral@novadireita.pt</a>, e a sua filiação torna-se efectiva a partir da data de pagamento da quota, conforme os estatutos do Partido. Se precisar de assistência durante o processo de pagamento ou tiver
                alguma dúvida sobre a sua filiação, não hesite em entrar em contacto connosco para o referido email. Estamos aqui para ajudar e garantir que sua experiência no ND seja positiva e gratificante.<br><br>
                Agradeço de coração pelo seu compromisso com o Nova Direita e aguardo ansiosamente para juntos trabalharmos em prol de nossos ideais comuns.<br><br>
                Cordialmente,<br><br>Ossanda Liber<br>Presidente da Comissão Política Nacional<br>Nova Direita
            </h3>
            <h5>
            <br><br>------------------------------------------------------------------------------------------------<br>
            AVISO DE CONFIDENCIALIDADE<br>
            Esta mensagem de correio electrónico e qualquer dos seus ficheiros anexos, caso existam, são confidenciais e destinados apenas á(s) pessoa(s) ou entidade(s) acima referida(s), podendo conter informação confidencial, privilegiada, a qual não deverá ser divulgada, copiada, gravada ou distribuída nos termos da lei vigente. Se não é o destinatário da mensagem, ou se ela lhe foi enviada por engano, agradecemos que não faça uso ou divulgação da mesma. A distribuição ou utilização da informação nela contida é VEDADA. Se recebeu esta mensagem por engano, por favor avise-nos de imediato, por correio electrónico, para o endereço acima e apague este e-mail do seu sistema. Obrigado.
            <br><br>
            CONFIDENTIALITY NOTICE
            <br>
            This e-mail transmission and eventual attached files are intended only for the use of the individual or entity named above and may contain information that is confidential, privileged and exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution or use of any of the information contained in this transmission is strictly VOIDED. If you have received this transmission in error, please notify us immediately by e-mail at the above address and delete this e-mail from your system. Thank you.
            </h5>
        </div>
        </body>
        </html>"""
        part2 = MIMEText(html, 'html')
        message.attach(part2)
        # Anexos PDF
        pdf_files = ["logos/nova_direita.png", "pdf/Principios.pdf", "pdf/Estatutos.pdf", "pdf/IBAN.pdf"]
        for pdf_file in pdf_files:
            try:
                with open(pdf_file, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), _subtype="pdf")
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_file)}')
                    message.attach(part)
            except FileNotFoundError as err:
                return f'Erro: Arquivo não encontrado - {pdf_file}. Erro: {err}'
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                server.login(self.sender_mail, self.password)
                server.sendmail(self.sender_mail, to, message.as_string())
                return f'Email enviado com sucesso para {to}'
        except smtplib.SMTPAuthenticationError as err:
            return f'Erro de autenticação SMTP: {err}'
        except Exception as err:
            return f'Ocorreu um erro ao enviar o email: {err}'
