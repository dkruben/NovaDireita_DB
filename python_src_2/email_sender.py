# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from utils import current_dir

# Construct the paths to the files using the current directory
pdf_files = [os.path.join(current_dir, '..', "src_files", "logos", "nova_direita.png"),
             os.path.join(current_dir, '..', "src_files", "pdf", "Principios.pdf"),
             os.path.join(current_dir, '..', "src_files", "pdf", "Estatutos.pdf"),
             os.path.join(current_dir, '..', "src_files", "pdf", "IBAN.pdf")]


class EmailSender:
    def __init__(self):
        self.from_email = os.getenv('SENDER_EMAIL', 'tomar@novadireita.pt')
        self.password = os.getenv('EMAIL_PASSWORD', 'BQr{E]2pmLU(')
        self.smtp_server = os.getenv('SMTP_SERVER', 'mail.novadireita.pt')
        self.smtp_port = int(os.getenv('SMTP_PORT', 465))

    def send_email(self, subject, body, to_email):
        msg = MIMEMultipart('alternative')
        msg['From'] = formataddr(('Nova Direita', self.from_email))
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, _charset='utf-8'))
        for pdf_file in pdf_files:
            try:
                with open(pdf_file, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), _subtype="pdf")
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_file)}')
                    msg.attach(part)
            except FileNotFoundError as err:
                print(f'Erro: Ficheiro não encontrado - {pdf_file}. Erro: {err}')

        # Send email
        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.from_email, self.password)
            server.sendmail(self.from_email, to_email, msg.as_string())
            server.quit()
            print(f"Email enviado com sucesso para: {to_email}")
        except smtplib.SMTPException as e:
            print(f"Falha ao enviar email: {str(e)}")
        except Exception as ex:
            print(f"Ocorreu um erro: {str(ex)}")
