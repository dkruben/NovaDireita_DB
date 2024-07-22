# -*- coding: utf-8 -*-
import mysql.connector
import pandas as pd
import pymysql

from database import DataBase
from email_sender import EmailSender
from print_pdf import PrintPdf
from sms_sender import send_sms


class Users(object):
    def __init__(self, idUser=0, name='', address='', city='', district='', cep='', phone='', nif='', cc='', cc_exp='', aniversario=None, email='', available=''):
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
        self.email_opts = EmailSender()
        # server settings
        self.host = DataBase().host
        self.user = DataBase().user
        self.password = DataBase().password
        self.database = DataBase().database
    
    def insert_militant(self):
        try:
            c = self.conn.cursor()
            c.execute('INSERT INTO militancy (nome, endereco, cidade, distrito, codPostal, telefone, nif, cc, cc_exp, data_nascimento, email, disponivel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available))
            self.conn.commit()
            # email
            self.email_opts.send_email(self.email, self.email_opts.sender_mail, self.email_opts.password, self.name)
            send_sms(f'+351{self.phone}')
            c.close()
            return f"Militante {self.name} adicionado com sucesso!"
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                return "Acesso negado. Verifique as credenciais da sua base de dados."
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                return "O base de dados não existe. Verifique o nome da base de dados."
            else:
                return f"Erro ao inserir o militante {self.name}: {err}"
        except Exception as err:
            return f"Ocorreu um erro inesperado: {err}"
    
    def update_militant(self):
        try:
            c = self.conn.cursor()
            c.execute("UPDATE militancy SET nome=%s, endereco=%s, cidade=%s, distrito=%s, codPostal=%s, telefone=%s, nif=%s, cc=%s, cc_exp=%s, data_nascimento=%s, email=%s, disponivel=%s WHERE militante=%s", (self.name, self.address, self.city, self.district, self.cep, self.phone, self.nif, self.cc, self.cc_exp, self.calendar_date, self.email, self.available, self.idUser))
            self.conn.commit()
            c.close()
            return f'Militante {self.name} atualizado com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na alteração dos dados do militante {err}'
    
    def delete_militant(self):
        try:
            c = self.conn.cursor()
            c.execute("DELETE FROM militancy WHERE militante = %s", (self.idUser,))
            self.conn.commit()
            c.close()
            return f'Militante {self.name} excluído com sucesso!'
        except Exception as err:
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
            return 'Militante encontrado com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na procura do militante. {err}'
    
    def create_sheet(self):
        try:
            c = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            query = 'select * from militancy'
            data = pd.read_sql(query, c)
            c.close()
            data.to_excel('lista_militantes.xlsx', index=False)
            return 'Arquivo criado com sucesso!'
        except pymysql.MySQLError as mysql_err:
            return f'Ocorreu um erro MySQL ao criar o arquivo: {mysql_err}'
        except pd.errors.EmptyDataError:
            return 'Nenhum dado retornado pela consulta SQL.'
        except Exception as err:
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
            return 'PDF gerado com sucesso!'
        except Exception as err:
            return f'Ocorreu um erro na criação do arquivo PDF: {err}'
