# -*- coding: utf-8 -*-
import logging
import os
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import scrolledtext, StringVar, Entry, Label, Button, Frame, Toplevel, INSERT, END, Radiobutton, Tk, LEFT, RIGHT, OptionMenu, WORD, BOTH
import ctypes
import subprocess
import sys
import mysql.connector
import pandas as pd
import pymysql
import pyuac
from fpdf import FPDF
from tkcalendar import DateEntry
from twilio.rest import Client

logger = logging.getLogger('NovaDireita')
logging.basicConfig(filename='militantes.log', filemode='w', datefmt='%d/%m/%Y %H:%M:%S', format='%(asctime)s [%(levelname)s]: %(name)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
logger.info('=====================LOG========================')


text_rgpd = (
    'Responsável pelo tratamento: Partido Nova Direita, com sede na Av. António Serpa 32 8b, 1050-027 Lisboa, Portugal; tlf: 217 961 260; email: todosjuntos@novadireita.pt. \n\n'
    'Finalidade do tratamento: inscrição e gestão da condição de militante na ND, cujo fundamento de licitude é o artigo 9.º, n.º 2, alínea d), do Regulamento Geral sobre a Proteção de Dados.\n\n'
    'Podem os dados pessoais do militante ser objeto de processamento informático e de utilização no âmbito das atividades das estruturas internas e autónomas e diferentes candidaturas eleitorais\n'
    'internas de militantes recebidas, nos termos dos Estatutos e dos Regulamentos Eleitorais do Partido Nova Direita,\n'
    'com a garantia de não serem divulgados a outras entidades para outras atividades que não se enquadrem no âmbito das atividades do Partido.\n'
    'Caso se venha a equacionar a cedência de dados a terceiros para uma finalidade legítima, tal carecerá sempre da obtenção prévia do consentimento do militante.\n\n'
    'Prazo de conservação: os seus dados serão conservados enquanto perdurar a condição de militante e, caso se aplique alguma\nnorma estatutária ou regulamentar que implique a conservação dos dados para lá desse momento,\n'
    'nomeadamente de ordem disciplinar, até ao final do prazo estatutariamente ou em regulamento previsto para a efetivação dessa norma.\n\n'
    'Direitos dos titulares: O titular dos dados pode exercer os seus direitos de acesso, retificação, oposição, eliminação ou limitação dos seus dados pessoais, nos termos do RGPD, devendo,\n'
    'para o efeito, remeter o seu pedido, por escrito, para militantes@novadireita.pt.\n\n'
    'Encarregado de Proteção de Dados: Em cumprimento do RGPD, o Encarregado da Proteção de Dados pode ser\ncontactado através do endereço eletrónico militantes@novadireita.pt.\n\n'
    'Direito de queixa: caso assim o entenda, o titular dos dados tem o direito de apresentar queixa junto da\nautoridade de controlo nacional, a Comissão Nacional de Proteção de Dados. Declaro sob compromisso de honra\n\n'
    'que todos os dados indicados aqui correspondem à verdade e que não me encontro numa das situações\nprevistas na Lei, nos Estatutos Nacionais do Partido e dos seus Regulamentos internos que impossibilitem a minha inscrição.')

district_options = ['Aveiro', 'Beja', 'Braga', 'Bragança', 'Castelo Branco', 'Coimbra', 'Évora', 'Faro', 'Guarda',
                    'Leiria', 'Lisboa', 'Portalegre', 'Porto', 'Santarém', 'Setúbal', 'Viana do Castelo', 'Vila Real',
                    'Viseu', 'Região Autónoma da Madeira', 'Região Autónoma dos Açores']


class DataBase(object):
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'militancy'
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        except Exception as err:
            logger.error(f'Erro ao conectar ao banco de dados {err}')
        self.createTable()
    
    def createTable(self):
        try:
            c = self.conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS militancy (militante INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), endereço VARCHAR(255), cidade VARCHAR(255), distrito VARCHAR(255), codPostal VARCHAR(255), telefone INT, nif INT, cc INT, data_nascimento DATE, email VARCHAR(255), disponível VARCHAR(255))')
            self.conn.commit()
            c.close()
        except Exception as err:
            logger.error(f'Erro ao criar a tabela de militantes: {str(err)}')


banco = DataBase()


class PrintPdf(FPDF):
    def header(self):
        self.image('../src_files/icon/nova_direita.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Lista de Militantes', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, name):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, name, 0, 1, 'L', True)
        self.ln(4)
    
    def chapter_body(self, body):
        with open(body, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, txt)
        self.ln()
    
    def print_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)


class Users(object):
    def __init__(self, idUser=0, name='', address='', city='', district='', cep='', phone='', nif='', cc='', aniversario=None, email='', available=''):
        self.info = {}
        self.idUser = idUser
        self.name = name
        self.address = address
        self.city = city
        self.district = district
        self.cep = cep
        self.phone = phone
        self.nif = nif
        self.cc = cc
        self.calendar_date = aniversario
        self.email = email
        self.available = available
        # email
        self.sender = ['tomar@novadireita.pt', 'BQr{E]2pmLU(']
        # server settings
        self.host = banco.host
        self.user = banco.user
        self.password = banco.password
        self.database = banco.database
    
    def insert_militant(self):
        try:
            c = banco.conn.cursor()
            c.execute('INSERT INTO militancy (nome, endereço, cidade, distrito, codPostal, telefone, nif, cc, data_nascimento, email, disponível) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.calendar_date, self.email, self.available))
            banco.conn.commit()
            # email
            self.send_email(self.email, self.sender[0], self.sender[1])
            self.send_sms(f'+351{self.phone}')
            c.close()
            logger.info('Militante registado com sucesso!')
            return 'Militante registado com sucesso!'
        except Exception as err:
            logger.error(f'Ocorreu um erro na adição do militante {err}')
            return 'Ocorreu um erro na adição do militante'
    
    def update_militant(self):
        try:
            c = banco.conn.cursor()
            c.execute("UPDATE militancy SET Nome=%s, endereço=%s, cidade=%s, distrito=%s, codPostal=%s, telefone=%s, nif=%s, cc=%s, data_nascimento=%s, email=%s, Disponível=%s WHERE militante=%s", (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.calendar_date, self.email, self.available, self.idUser))
            banco.conn.commit()
            c.close()
            logger.info('Militante atualizado com sucesso!')
            return 'Militante atualizado com sucesso!'
        except Exception as err:
            logger.error(f'Ocorreu um erro na alteração dos dados do militante {err}')
            return 'Ocorreu um erro na alteração dos dados do militante'
    
    def delete_militant(self):
        try:
            c = banco.conn.cursor()
            c.execute("DELETE FROM militancy WHERE militante = %s", (self.idUser,))
            banco.conn.commit()
            c.close()
            logger.info('Militante excluído com sucesso!')
            return 'Militante excluído com sucesso!'
        except Exception as err:
            logger.error(f'Ocorreu um erro na exclusão do militante {err}')
            return 'Ocorreu um erro na exclusão do militante'
    
    def select_militant(self, idUser):
        c = banco.conn.cursor()
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
                self.calendar_date = row[9]
                self.email = row[9]
                self.available = row[10]
            c.close()
            logger.info('Militante encontrado com sucesso!')
            return 'Procura feita com sucesso!'
        except Exception as err:
            logger.error(f'Ocorreu um erro na procura do militante. {err}')
            return 'Ocorreu um erro na procura do militante'
    
    def send_email(self, to, sender_email, password):
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
                <h2>"""  f'Saudações, sr.(a) {self.name}!' """</h2>
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
        pdf_files = ["icon/nova_direita.png", "pdf/Princípios.pdf", "pdf/Estatutos.pdf", "pdf/IBAN.pdf"]
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
                logger.info(f'Email enviado com sucesso para {to}')
                return f'Email enviado com sucesso para {to}'
            except smtplib.SMTPAuthenticationError as err:
                logger.error(f'Erro de autenticação SMTP: {err}')
                logger.info('Verifique o nome de usuário, a senha e o acesso a \'aplicativos menos seguros\'.')
            except Exception as err:
                logger.error(f'Um erro ocorreu: {err}')
    
    @staticmethod
    def send_sms(to_number):
        account_sid = 'ACdf255c5db2239e5616b057e2b1024c45'
        auth_token = 'eeb7bc044903daa4ba55e4a8610cd54e'
        client = Client(account_sid, auth_token)
        from_number = '+18149147506'
        try:
            message = 'Bem-vindo à Nova Direita! A sua filiação foi efectuada com sucesso. Dentro de instantes receberá um Email com os dados para pagamento das suas quotas. Agradecemos a sua colaboração e esperamos que a sua experiência na ND seja positiva e gratificante.'
            message = client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )
            logger.info(f'SMS sent successfully. Message SID: {message.sid}')
            return f'SMS sent successfully. Message SID: {message.sid}'
        except Exception as err:
            logger.error(f'Erro ao enviar SMS: {err}')
            logger.info('Verifique o número de telefone e o acesso a \'aplicativos menos seguros\'.')
            return f'Erro ao enviar SMS: {err}'
    
    def create_sheet(self):
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            query = 'select * from militancy'
            data = pd.read_sql(query, conn)
            conn.close()
            data.to_excel('militancy.xlsx', index=False)
            logger.info('Arquivo criado com sucesso!')
            return 'Arquivo criado com sucesso!'
        except pymysql.MySQLError as mysql_err:
            logger.error(f'Ocorreu um erro MySQL ao criar o arquivo: {mysql_err}')
            return f'Ocorreu um erro MySQL ao criar o arquivo: {mysql_err}'
        except pd.errors.EmptyDataError:
            logger.error('Nenhum dado retornado pela consulta SQL.')
            return 'Nenhum dado retornado pela consulta SQL.'
        except Exception as err:
            logger.error(f'Ocorreu um erro na criação do arquivo: {err}')
            return f'Ocorreu um erro na criação do arquivo: {err}'
    
    @staticmethod
    def generate_pdf():
        try:
            pdf = PrintPdf()
            pdf.add_page()
            c = banco.conn.cursor()
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
                pdf.cell(0, 5, f'Data de Nascimento: {row[9]}', 0, 1)
                pdf.cell(0, 5, f'E-mail: {row[10]}', 0, 1)
                pdf.cell(0, 5, f'Disponível: {row[11]}', 0, 1)
                pdf.ln(10)
            pdf_file = 'lista_militantes.pdf'
            pdf.output(pdf_file)
            logger.info('PDF gerado com sucesso!')
            return 'PDF gerado com sucesso!'
        except Exception as err:
            logger.error(f'Ocorreu um erro na criação do arquivo PDF: {err}')
            return 'Ocorreu um erro na criação do arquivo PDF'


user = Users()


class Application:
    def __init__(self, master=None):
        self.lbl_font = ('Cambria', '12', 'bold')
        self.txt_font = ('times new roman', '11')
        self.radio = StringVar()
        # Militante
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()
        # Procurar
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()
        # Nome
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 5
        self.container3.pack()
        # Endereço
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()
        # Cidade
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 5
        self.container5.pack()
        # Distrito
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 5
        self.container6.pack()
        # Cód. Postal
        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5
        self.container7.pack()
        # Telefone
        self.container8 = Frame(master)
        self.container8['padx'] = 20
        self.container8['pady'] = 5
        self.container8.pack()
        # NIF
        self.container9 = Frame(master)
        self.container9['padx'] = 20
        self.container9['pady'] = 5
        self.container9.pack()
        # BI/CC
        self.container10 = Frame(master)
        self.container10['padx'] = 20
        self.container10['pady'] = 5
        self.container10.pack()
        # Calendário
        self.container11 = Frame(master)
        self.container11['padx'] = 20
        self.container11['pady'] = 5
        self.container11.pack()
        # E-mail
        self.container12 = Frame(master)
        self.container12['padx'] = 20
        self.container12['pady'] = 5
        self.container12.pack()
        # RGPD
        self.btn_open_second_window = Button(master, text='Termos e Condições', font=self.lbl_font, width=16, bg='purple', fg='white')
        self.btn_open_second_window['padx'] = 20
        self.btn_open_second_window['pady'] = 5
        self.btn_open_second_window['command'] = self.openSecondWindow
        self.btn_open_second_window.pack()
        # Disponível
        self.container13 = Frame(master)
        self.container13['padx'] = 20
        self.container13['pady'] = 5
        self.container13.pack()
        # Inserir
        self.container14 = Frame(master)
        self.container14['pady'] = 15
        self.container14.pack()
        # Alterar
        self.container15 = Frame(master)
        self.container15['pady'] = 15
        self.container15.pack()
        # Excluir
        self.container16 = Frame(master)
        self.container16['pady'] = 15
        self.container16.pack()
        # Sair
        self.title = Label(self.container1, text='Gestão de Militantes:')
        self.title['font'] = self.lbl_font
        self.title.pack()
        # Militante
        self.lbl_idUser = Label(self.container2, text='Militante:', font=self.lbl_font, width=10)
        self.lbl_idUser.pack(side=LEFT)
        self.txt_idUser = Entry(self.container2)
        self.txt_idUser['width'] = 14
        self.txt_idUser['font'] = self.txt_font
        self.txt_idUser.pack(side=LEFT)
        # Procurar
        self.btn_search = Button(self.container2, text='Procurar', font=self.lbl_font, width=10)
        self.btn_search['command'] = self.search_militant
        self.btn_search.pack(side=RIGHT)
        # Nome
        self.lbl_name = Label(self.container3, text='Nome:', font=self.lbl_font, width=10)
        self.lbl_name.pack(side=LEFT)
        self.txt_name = Entry(self.container3)
        self.txt_name['width'] = 125
        self.txt_name['font'] = self.txt_font
        self.txt_name.pack(side=LEFT)
        # Endereço
        self.lbl_address = Label(self.container4, text='Endereço:', font=self.lbl_font, width=10)
        self.lbl_address.pack(side=LEFT)
        self.txt_address = Entry(self.container4)
        self.txt_address['width'] = 125
        self.txt_address['font'] = self.txt_font
        self.txt_address.pack(side=LEFT)
        # Cidade
        self.lbl_city = Label(self.container5, text='Cidade:', font=self.lbl_font, width=10)
        self.lbl_city.pack(side=LEFT)
        self.txt_city = Entry(self.container5)
        self.txt_city['width'] = 125
        self.txt_city['font'] = self.txt_font
        self.txt_city.pack(side=LEFT)
        # Distrito
        self.lbl_district = Label(self.container6, text='Distrito:', font=self.lbl_font, width=10)
        self.lbl_district.pack(side=LEFT)
        self.selected_district = StringVar()
        self.selected_district.set(district_options[10])
        self.dropdown_district = OptionMenu(self.container6, self.selected_district, *district_options)
        self.dropdown_district.pack(side=LEFT)
        # Cód. Postal
        self.lbl_cep = Label(self.container7, text='Cód. Postal:', font=self.lbl_font, width=10)
        self.lbl_cep.pack(side=LEFT)
        self.txt_cep = Entry(self.container7)
        self.txt_cep['width'] = 125
        self.txt_cep['font'] = self.txt_font
        self.txt_cep.pack(side=LEFT)
        # Telefone
        self.lbl_phone = Label(self.container8, text='Telefone:', font=self.lbl_font, width=10)
        self.lbl_phone.pack(side=LEFT)
        self.txt_phone = Entry(self.container8)
        self.txt_phone['width'] = 125
        self.txt_phone['font'] = self.txt_font
        self.txt_phone.pack(side=LEFT)
        # NIF
        self.lbl_nif = Label(self.container9, text='NIF:', font=self.lbl_font, width=10)
        self.lbl_nif.pack(side=LEFT)
        self.txt_nif = Entry(self.container9)
        self.txt_nif['width'] = 125
        self.txt_nif['font'] = self.txt_font
        self.txt_nif.pack(side=LEFT)
        # BI/CC
        self.lbl_cc = Label(self.container10, text='BI/CC:', font=self.lbl_font, width=10)
        self.lbl_cc.pack(side=LEFT)
        self.txt_cc = Entry(self.container10)
        self.txt_cc['width'] = 125
        self.txt_cc['font'] = self.txt_font
        self.txt_cc.pack(side=LEFT)
        # Calendar
        self.lbl_calendar = Label(self.container11, text='Data de Nascimento:', font=self.lbl_font)
        self.lbl_calendar.pack(side=LEFT, padx=10, pady=5)
        frame_calendar = Frame(self.container11)
        frame_calendar.pack(side=LEFT)
        self.entry_calendar = DateEntry(frame_calendar, width=12, font=self.txt_font, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.entry_calendar.pack(side=LEFT)
        # E-mail
        self.lbl_email = Label(self.container12, text='E-mail:', font=self.lbl_font, width=10)
        self.lbl_email.pack(side=LEFT)
        self.txt_email = Entry(self.container12)
        self.txt_email['width'] = 125
        self.txt_email['font'] = self.txt_font
        self.txt_email.pack()
        # Disponível
        self.lbl_available = Label(self.container13, text='Aceito os termos acima?', font=self.lbl_font, width=30)
        self.lbl_available.pack(side=LEFT)
        self.box_available_1 = Radiobutton(self.container13, text='Sim', font=self.txt_font, variable=self.radio, value='Sim')
        self.box_available_1.pack(side=LEFT)
        self.box_available_2 = Radiobutton(self.container13, text='Não', font=self.txt_font, variable=self.radio, value='Não')
        self.box_available_2.pack(side=LEFT)
        # Inserir
        self.bnt_insert = Button(self.container14, text='Inserir', font=self.lbl_font, width=12, bg='green', fg='white')
        self.bnt_insert['command'] = self.insert_militant
        self.bnt_insert.pack(side=LEFT)
        # Alterar
        self.bnt_change = Button(self.container14, text='Alterar', font=self.lbl_font, width=12, bg='orange', fg='white')
        self.bnt_change['command'] = self.change_militant
        self.bnt_change.pack(side=LEFT)
        # Excluir
        self.bnt_delete = Button(self.container14, text='Excluir', font=self.lbl_font, width=12, bg='red', fg='white')
        self.bnt_delete['command'] = self.exclude_militant
        self.bnt_delete.pack(side=LEFT)
        # Exportar Sheets
        self.bnt_export = Button(self.container15, text='Exportar Exel', font=self.lbl_font, width=12, bg='blue', fg='white')
        self.bnt_export['command'] = self.export_sheets
        self.bnt_export.pack(side=LEFT)
        # Exportar PDF
        self.bnt_export_pdf = Button(self.container15, text='Exportar PDF', font=self.lbl_font, width=12, bg='pink', fg='white')
        self.bnt_export_pdf['command'] = self.export_pdf
        self.bnt_export_pdf.pack(side=LEFT)
        # Sair
        self.bnt_exit = Button(self.container15, text='Sair', font=self.lbl_font, width=12, bg='gray', fg='white')
        self.bnt_exit['command'] = root.destroy
        self.bnt_exit.pack(side=LEFT)
        # Mensagem
        self.lbl_msg = Label(self.container16, text='', fg='blue')
        self.lbl_msg['font'] = ('Verdana', '9', 'bold')
        self.lbl_msg.pack()
    
    def openSecondWindow(self):
        second_window = Toplevel()
        second_window.title("Termos e Condições")
        second_window.geometry("600x500")
        # second_window.iconbitmap('../src_files/icon/logo.ico')
        second_window.transient(root)
        second_window.focus_force()
        second_window.grab_set()
        text_area = scrolledtext.ScrolledText(second_window, wrap=WORD, font=self.txt_font)
        text_area.insert(END, text_rgpd)
        text_area.configure(state='disabled')
        text_area.pack(fill=BOTH, expand=True, padx=10, pady=10)
        close_button = Button(second_window, text='Fechar', command=second_window.destroy, width=12, bg='red', fg='black')
        close_button.pack(pady=10)
        second_window.update_idletasks()
        width = second_window.winfo_width()
        height = second_window.winfo_height()
        x = (second_window.winfo_screenwidth() // 2) - (width // 2)
        y = (second_window.winfo_screenheight() // 2) - (height // 2)
        second_window.geometry(f'{width}x{height}+{x}+{y}')
        second_window.bind('<Escape>', lambda event: second_window.destroy())
    
    def insert_militant(self):
        user.name = self.txt_name.get()
        user.address = self.txt_address.get()
        user.city = self.txt_city.get()
        user.district = self.selected_district.get()
        user.cep = self.txt_cep.get()
        user.phone = self.txt_phone.get()
        user.nif = self.txt_nif.get()
        user.cc = self.txt_cc.get()
        user.calendar_date = self.entry_calendar.get_date()
        user.email = self.txt_email.get()
        user.available = self.radio.get()
        # Verificar se o campo 'nome' está preenchido
        if not user.name:
            self.lbl_msg['text'] = 'Campo "Nome" é obrigatório.'
            return
        # Verificar se o campo 'Morada' está preenchido
        if not user.address:
            self.lbl_msg['text'] = 'Campo "Morada" é obrigatório.'
            return
        # Verificar se o campo 'Cidade' está preenchido
        if not user.city:
            self.lbl_msg['text'] = 'Campo "Cidade" é obrigatório.'
            return
        # Verificar se o campo 'Distrito' está preenchido
        if not user.district:
            self.lbl_msg['text'] = 'Campo "Distrito" é obrigatório.'
            return
        # Verificar se o campo 'Código Postal' está preenchido
        if not user.cep:
            self.lbl_msg['text'] = 'Campo "Código Postal" é obrigatório.'
            return
        # Verificar se o campo 'Telefone' está preenchido
        if not user.phone and not user.phone.isnumeric():
            self.lbl_msg['text'] = 'Campo "Telefone" é obrigatório.'
            return
        # Verificar se o campo 'N.I.F' está preenchido
        if not user.nif and not user.nif.isnumeric():
            self.lbl_msg['text'] = 'Campo "N.I.F" é obrigatório.'
            return
        # Verificar se o campo 'BI/CC' está preenchido
        if not user.cc and not user.cc.isnumeric():
            self.lbl_msg['text'] = 'Campo "BI/CC" é obrigatório.'
            return
        # Verificar se o campo 'Data de Nascimento' está preenchido
        if not user.calendar_date:
            self.lbl_msg['text'] = 'Campo "Data de Nascimento" é obrigatório.'
            return
        # Verificar se o campo 'Email' está preenchido
        if not user.email:
            self.lbl_msg['text'] = 'Campo "Email" é obrigatório.'
            return
        # Verificar se o campo 'Termos' está preenchido
        if not (self.openSecondWindow and user.available):
            self.lbl_msg['text'] = 'Você precisa de aceitar os termos e condições para continuar.'
            return
        # Limpar os campos após a operação
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        user.district = self.selected_district.get()
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
        self.radio.get()
        self.lbl_msg['text'] = user.insert_militant()
        self.clear_fields()
    
    def change_militant(self):
        user.idUser = self.txt_idUser.get()
        user.name = self.txt_name.get()
        user.address = self.txt_address.get()
        user.city = self.txt_city.get()
        user.district = self.selected_district.get()
        user.cep = self.txt_cep.get()
        user.phone = self.txt_phone.get()
        user.nif = self.txt_nif.get()
        user.cc = self.txt_cc.get()
        user.calendar_date = self.entry_calendar.get_date()
        user.email = self.txt_email.get()
        user.available = self.radio.get()
        #
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.selected_district.set(user.district)
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
        self.radio.get()
        self.lbl_msg['text'] = user.update_militant()
        self.clear_fields()
    
    def exclude_militant(self):
        user.idUser = self.txt_idUser.get()
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.selected_district.set(user.district)
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
        self.lbl_msg['text'] = user.delete_militant()
        self.clear_fields()
    
    def export_sheets(self):
        self.lbl_msg['text'] = user.create_sheet()
    
    def export_pdf(self):
        self.lbl_msg['text'] = user.generate_pdf()
    
    def search_militant(self):
        userId = user.idUser
        idUser = self.txt_idUser.get()
        self.txt_idUser.delete(0, END)
        self.txt_idUser.insert(INSERT, userId)
        self.txt_name.delete(0, END)
        self.txt_name.insert(INSERT, user.name)
        self.txt_address.delete(0, END)
        self.txt_address.insert(INSERT, user.address)
        self.txt_city.delete(0, END)
        self.txt_city.insert(INSERT, user.city)
        self.selected_district.set(user.district)
        self.txt_cep.delete(0, END)
        self.txt_cep.insert(INSERT, user.cep)
        self.txt_phone.delete(0, END)
        self.txt_phone.insert(INSERT, user.phone)
        self.txt_nif.delete(0, END)
        self.txt_nif.insert(INSERT, user.nif)
        self.txt_cc.delete(0, END)
        self.txt_cc.insert(INSERT, user.cc)
        self.entry_calendar.delete(0, END)
        self.entry_calendar.set_date(user.calendar_date)
        self.txt_email.delete(0, END)
        self.txt_email.insert(INSERT, user.email)
        self.radio.set(user.available)
        self.lbl_msg['text'] = user.select_militant(idUser)
        self.fill_fields()
    
    def clear_fields(self):
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.selected_district.set(user.district)
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
    
    def fill_fields(self):
        self.txt_idUser.delete(0, END)
        self.txt_idUser.insert(INSERT, user.idUser)
        self.txt_name.delete(0, END)
        self.txt_name.insert(INSERT, user.name)


if __name__ == '__main__':
    if os.name == 'nt':
        # if not ctypes.windll.shell32.IsUserAnAdmin():
        #    subprocess.run(["NovaDireita.exe", sys.executable, *sys.argv])
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
        else:
            root = Tk()
            root.withdraw()  # Hide the root window initially
            Application(root)
            root.title('Nova Direita - Gestão de Militantes')
            root.geometry('800x700')
            # root.iconbitmap('../src_files/icon/logo.ico')
            root.deiconify()  # Show the root window after setting up the application
            root.mainloop()
    else:
        root = Tk()
        root.withdraw()  # Hide the root window initially
        Application(root)
        root.title('Nova Direita - Gestão de Militantes')
        root.geometry('800x700')
        # root.iconbitmap('../src_files/icon/logo.ico')
        root.deiconify()  # Show the root window after setting up the application
        root.mainloop()
