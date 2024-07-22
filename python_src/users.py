# -*- coding: utf-8 -*-
import os
import mysql.connector
import pandas as pd
import pymysql

from database import DataBase
from email_sender import EmailSender
from print_pdf import PrintPdf
from sms_sender import send_sms


class Users:
    """Class to handle user (militant) operations in the database."""
    def __init__(self, idUser=0, name='', address='', city='', district='', cep='', phone='', nif='', cc='', cc_exp='', aniversario=None, email='', available=''):
        # Database connection and user attributes
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
        # Email sender instance
        self.email_sender = EmailSender()
        # Server settings
        self.host = DataBase().host
        self.user = DataBase().user
        self.password = DataBase().password
        self.database = DataBase().database
    
    def insert_militant(self):
        """Insert a new militant into the database."""
        try:
            cursor = self.conn.cursor()
            query = '''INSERT INTO militancy(nome, endereco, cidade, distrito, codPostal, telefone, nif, cc, cc_exp, data_nascimento, email, disponivel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            values = (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available)
            cursor.execute(query, values)
            self.conn.commit()
            # Notify via email and SMS
            self.email_sender.send_email(self.email, self.name)
            send_sms(f'+351{self.phone}')
            
            cursor.close()
            return f"Militante {self.name} adicionado com sucesso!"
        except mysql.connector.Error as err:
            return self.handle_mysql_error(err)
        except Exception as err:
            return f"Ocorreu um erro inesperado: {err}"
    
    def update_militant(self):
        """Update an existing militant's details."""
        try:
            cursor = self.conn.cursor()
            query = '''UPDATE militancy SET nome=%s, endereco=%s, cidade=%s, distrito=%s, codPostal=%s, telefone=%s, nif=%s, cc=%s, cc_exp=%s, data_nascimento=%s, email=%s, disponivel=%s WHERE militante=%s'''
            values = (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available, self.idUser)
            cursor.execute(query, values)
            self.conn.commit()
            cursor.close()
            return f'Militante {self.name} atualizado com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na alteração dos dados do militante: {err}'
    
    def delete_militant(self):
        """Delete a militant from the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM militancy WHERE militante = %s", (self.idUser,))
            self.conn.commit()
            cursor.close()
            return f'Militante {self.name} excluído com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na exclusão do militante: {err}'
    
    def select_militant(self, idUser):
        """Retrieve a militant's information from the database."""
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM militancy WHERE militante = %s"
            cursor.execute(query, (idUser,))
            result = cursor.fetchone()
            if result:
                self.idUser, self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available = result
            cursor.close()
            return 'Militante encontrado com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na procura do militante: {err}'
    
    def create_sheet(self):
        """Create an Excel sheet of militants."""
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            query = 'SELECT * FROM militancy'
            data = pd.read_sql(query, conn)
            conn.close()
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            export_folder = os.path.join(desktop_path, 'Lista exportada')
            if not os.path.exists(export_folder):
                os.makedirs(export_folder)
            excel_file = os.path.join(export_folder, 'lista_militantes.xlsx')
            data.to_excel(excel_file, index=False)
            return 'Arquivo criado com sucesso!'
        except pymysql.MySQLError as mysql_err:
            return f'Ocorreu um erro MySQL ao criar o arquivo: {mysql_err}'
        except pd.errors.EmptyDataError:
            return 'Nenhum dado retornado pela consulta SQL.'
        except Exception as err:
            return f'Ocorreu um erro na criação do arquivo: {err}'
    
    def generate_pdf(self):
        """Generate a PDF document listing militants."""
        try:
            pdf = PrintPdf()
            pdf.add_page()
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM militancy')
            rows = cursor.fetchall()
            pdf.set_font('Arial', '', 10)
            for row in rows:
                pdf.chapter_title(f'Militante: {row[0]}')
                for i, field in enumerate(['Nome', 'Endereço', 'Cidade', 'Distrito', 'Código Postal', 'Telefone', 'NIF', 'Cartão de Cidadão', 'Validade Cartão de Cidadão', 'Data de Nascimento', 'E-mail', 'Disponível']):
                    pdf.cell(0, 5, f'{field}: {row[i + 1]}', 0, 1)
                pdf.ln(10)
            cursor.close()
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            export_folder = os.path.join(desktop_path, 'Lista exportada')
            if not os.path.exists(export_folder):
                os.makedirs(export_folder)
            pdf_file = os.path.join(export_folder, 'lista_militantes.pdf')
            pdf.output(pdf_file)
            return 'PDF gerado com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na criação do arquivo PDF: {err}'
    
    @staticmethod
    def handle_mysql_error(err):
        """Handle MySQL errors."""
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            return "Acesso negado. Verifique as credenciais da sua base de dados."
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            return "O base de dados não existe. Verifique o nome da base de dados."
        else:
            return f"Erro ao inserir o militante: {err}"
