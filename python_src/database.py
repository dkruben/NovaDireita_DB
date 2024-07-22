# -*- coding: utf-8 -*-
from tkinter import messagebox

import mysql.connector


class DataBase(object):
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'militancy'
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        except Exception as err:
            messagebox.showerror('Erro', f'Erro ao conectar ao banco de dados {err}')
        self.createTable()
    
    def createTable(self):
        try:
            c = self.conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS militancy (militante INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), endereco VARCHAR(255), cidade VARCHAR(255), distrito VARCHAR(255), codPostal VARCHAR(10), telefone VARCHAR(15), nif VARCHAR(10), cc VARCHAR(10), cc_exp DATE, data_nascimento DATE, email VARCHAR(255), disponivel VARCHAR(3))')
            self.conn.commit()
            c.close()
        except Exception as err:
            messagebox.showerror('Erro', f'Erro ao criar a tabela de militantes: {str(err)}')


banc = DataBase()
