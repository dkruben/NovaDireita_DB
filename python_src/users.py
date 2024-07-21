# -*- coding: utf-8 -*-
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mysql.connector
import pandas as pd
import pymysql
from twilio.rest import Client

from database import DataBase
# from loggin_setup import logger
from print_pdf import PrintPdf


class Users(object):
    def __init__(self, idUser=0, name='', address='', city='', district='', cep='', phone='', nif='', cc='', cc_exp='', aniversario=None, email='', available=''):
        # logger.info(f"Criar um novo Militante: {name}")
        self.conn = DataBase().conn
        self.idUser = idUser
        self.name = name
        self.address = address
        self.city = city
        self.district = district
        self.cep = cep
        self.phone = phone
        self.nif = nif
        self.cc = cc
        self.cc_exp = cc_exp
        self.calendar_date = aniversario
        self.email = email
        self.available = available
        # email
        self.sender = ['tomar@novadireita.pt', 'BQr{E]2pmLU(']
        # server settings
        self.host = DataBase().host
        self.user = DataBase().user
        self.password = DataBase().password
        self.database = DataBase().database
    
    def insert_militant(self):
        # logger.info(f"Adicionar Militante na base de dados: {self.name}")
        try:
            c = self.conn.cursor()
            c.execute('INSERT INTO militancy (nome, endereco, cidade, distrito, codPostal, telefone, nif, cc, cc_exp, data_nascimento, email, disponivel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available))
            self.conn.commit()
            # logger.info(f"Militante {self.name} adicionado com sucesso!")
            # email
            self.send_email(self.email, self.sender[0], self.sender[1])
            self.send_sms(f'+351{self.phone}')
            c.close()
            return f"Militante {self.name} adicionado com sucesso!"
        except mysql.connector.Error as err:
            # logger.error(f"Erro ao inserir militante {self.name}: {err}")
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                return "Acesso negado. Verifique as credenciais da sua base de dados."
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                return "O base de dados não existe. Verifique o nome da base de dados."
            else:
                return f"Erro ao inserir o militante {self.name}: {err}"
        except Exception as err:
            # logger.error(f"Ocorreu um erro inesperado: {err}")
            return f"Ocorreu um erro inesperado: {err}"
    
    def update_militant(self):
        try:
            c = self.conn.cursor()
            c.execute("UPDATE militancy SET nome=%s, endereco=%s, cidade=%s, distrito=%s, codPostal=%s, telefone=%s, nif=%s, cc=%s, cc_exp=%s, data_nascimento=%s, email=%s, disponivel=%s WHERE militante=%s", (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available, self.idUser))
            self.conn.commit()
            c.close()
            # logger.info(f'Militante {self.name} atualizado com sucesso!')
            return f'Militante {self.name} atualizado com sucesso!'
        except Exception as err:
            # logger.error(f'Ocorreu um erro na alteração dos dados do militante {err}')
            return f'Ocorreu um erro na alteração dos dados do militante {err}'
    
    def delete_militant(self):
        try:
            c = self.conn.cursor()
            c.execute("DELETE FROM militancy WHERE militante = %s", (self.idUser,))
            self.conn.commit()
            c.close()
            # logger.info(f'Militante {self.name} excluído com sucesso!')
            return f'Militante {self.name} excluído com sucesso!'
        except Exception as err:
            # logger.error(f'Ocorreu um erro na exclusão do militante {err}')
            return f'Ocorreu um erro na exclusão do militante {err}'
    
    def select_militant(self, idUser):
        c = self.conn.cursor()
        query = "SELECT * FROM militancy WHERE militante = %s"
        c.execute(query, (idUser,))
        try:
            for row in c:
                self.idUser = row[0]
                self.name = row[1]
                self.address = row[2]
                self.city = row[3]
                self.district = row[4]
                self.cep = row[5]
                self.phone = row[6]
                self.nif = row[7]
                self.cc = row[8]
                self.cc_exp = row[9]
                self.calendar_date = row[10]
                self.email = row[11]
                self.available = row[12]
            c.close()
            # logger.info('Militante encontrado com sucesso!')
            return 'Militante encontrado com sucesso!'
        except Exception as err:
            # logger.error(f'Ocorreu um erro na procura do militante. {err}')
            return f'Ocorreu um erro na procura do militante. {err}'
    
    def send_email(self, to, sender_email, password):
        # logger.info(f"Sending welcome email to: {to}")
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Nova Direita - Inscrição'
        message['From'] = self.sender[0]
        message['To'] = to
        message['Importance'] = 'high'
        html = """
            <!DOCTYPE html>
            <html lang='pt'>
            <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>(no-reply) - Nova Direita</title>
            </head>
            <body>
            <div>
                <h2>"""f'Saudações, sr.(a) {self.name}!'"""/h2>
                <h3>
                    Em nome de toda a equipe do Nova Direita, é com grande prazer que confirmo a aceitação de sua filiação como membro activo de nosso Partido Político<br><br>
                    A sua decisão de se juntar a nós, é o testemunho do seu compromisso com os valores e objectivos que defendemos e implica a aceitação dos estatutos e declaração de princípios, aprovados no Congresso Fundador e que se encontram em anexo.<br>
                    Para começar a sua jornada connosco, gostaria de convidá-lo a efectuar o pagamento da sua quota anual de membro, no valor de 30€, para o IBAN do<br>
                    partido que se encontra em anexo. De seguida, envie o comprovativo para o email<br>
                    <a href="malito: secretariageral@novadireita.pt">secretariageral@novadireita.pt</a>, e a sua filiação torna-se efectiva a partir da data de pagamento da quota, conforme os estatutos do Partido. Se precisar de assistência durante o processo de pagamento ou tiver
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
            with open(pdf_file, "rb") as attachment:
                part = MIMEApplication(attachment.read(), _subtype="pdf")
                part.add_header('Content-Disposition', f'attachment; filename= {pdf_file}')
                message.attach(part)
        #
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('mail.novadireita.pt', 465, context=context) as server:
            try:
                server.login(sender_email, password)
                server.sendmail(sender_email, to, message.as_string())
                # logger.info(f'Email enviado com sucesso para {to}')
                return f'Email enviado com sucesso para {to}'
            except smtplib.SMTPAuthenticationError as err:
                # logger.error(f'Erro de autenticação SMTP: {err}')
                return f'Erro de autenticação SMTP: {err}'
                # logger.info('Verifique o nome de usuário, a senha e o acesso a \'aplicativos menos seguros\'.')
            except Exception as err:
                # logger.error(f'Ocurreu um erro: {err}')
                return f'Ocorreu um erro ao enviar o email: {err}'
    
    @staticmethod
    def send_sms(to_number):
        account_sid = 'ACdf255c5db2239e5616b057e2b1024c45'
        auth_token = 'eeb7bc044903daa4ba55e4a8610cd54e'
        client = Client(account_sid, auth_token)
        from_number = '+18149147506'  # Consider making this dynamic or configurable
        try:
            message = 'Bem-vindo à Nova Direita! A sua filiação foi efectuada com sucesso. Dentro de instantes receberá um Email com os dados para pagamento das suas quotas. Agradecemos a sua colaboração e esperamos que a sua experiência na ND seja positiva e gratificante.'
            message = client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )
            # logger.info(f'SMS sent successfully. Message SID: {message.sid}')
            return f'SMS sent successfully. Message SID: {message.sid}'
        except Exception as err:
            # logger.error(f'Erro ao enviar SMS: {err}')
            # logger.info('Verifique o número de telefone e o acesso a \'aplicativos menos seguros\'.')
            return f'Erro ao enviar SMS: {err}'
    
    def create_sheet(self):
        try:
            c = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            query = 'select * from militancy'
            data = pd.read_sql(query, c)
            c.close()
            data.to_excel('lista_militantes.xlsx', index=False)
            # logger.info('Arquivo criado com sucesso!')
            return 'Arquivo criado com sucesso!'
        except pymysql.MySQLError as mysql_err:
            # logger.error(f'Ocorreu um erro MySQL ao criar o arquivo: {mysql_err}')
            return f'Ocorreu um erro MySQL ao criar o arquivo: {mysql_err}'
        except pd.errors.EmptyDataError:
            # logger.error('Nenhum dado retornado pela consulta SQL.')
            return 'Nenhum dado retornado pela consulta SQL.'
        except Exception as err:
            # logger.error(f'Ocorreu um erro na criação do arquivo: {err}')
            return f'Ocorreu um erro na criação do arquivo: {err}'
    
    def generate_pdf(self):
        try:
            pdf = PrintPdf()
            pdf.add_page()
            c = self.conn.cursor()
            c.execute('select * from militancy')
            rows = c.fetchall()
            pdf.set_font('Arial', '', 10)
            for row in rows:
                pdf.chapter_title(f'Militante: {row[0]}')
                pdf.cell(0, 5, f'Nome: {row[1]}', 0, 1)
                pdf.cell(0, 5, f'Endereço: {row[2]}', 0, 1)
                pdf.cell(0, 5, f'Cidade: {row[3]}', 0, 1)
                pdf.cell(0, 5, f'Distrito: {row[4]}', 0, 1)
                pdf.cell(0, 5, f'Código Postal: {row[5]}', 0, 1)
                pdf.cell(0, 5, f'Telefone: {row[6]}', 0, 1)
                pdf.cell(0, 5, f'NIF: {row[7]}', 0, 1)
                pdf.cell(0, 5, f'Cartão de Cidadão: {row[8]}', 0, 1)
                pdf.cell(0, 5, f'Validade Cartão de Cidadão: {row[9]}', 0, 1)
                pdf.cell(0, 5, f'Data de Nascimento: {row[10]}', 0, 1)
                pdf.cell(0, 5, f'E-mail: {row[11]}', 0, 1)
                pdf.cell(0, 5, f'Disponível: {row[12]}', 0, 1)
                pdf.ln(10)
            c.close()
            pdf_file = 'lista_militantes.pdf'
            pdf.output(pdf_file)
            # logger.info('PDF gerado com sucesso!')
            return 'PDF gerado com sucesso!'
        except Exception as err:
            # logger.error(f'Ocorreu um erro na criação do arquivo PDF: {err}')
            return f'Ocorreu um erro na criação do arquivo PDF: {err}'
