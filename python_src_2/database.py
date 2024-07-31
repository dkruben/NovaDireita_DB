# -*- coding: utf-8 -*-
import mysql.connector
import wx

from constants import db_name


class Database:
    def __init__(self, host='localhost', user='root', password='', database=db_name):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.c = self.conn.cursor()
            self.create_table()
        except mysql.connector.Error as error:
            wx.MessageBox('Erro', f'Erro ao conectar ao banco de dados: {error}', wx.OK | wx.ICON_ERROR)

    def create_table(self):
        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS militantes (militant INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, address VARCHAR(255), district VARCHAR(100), city VARCHAR(100), parish VARCHAR(100), zip_code VARCHAR(10), phone VARCHAR(14), bi_cc VARCHAR(20), nif VARCHAR(9), email VARCHAR(100), birthday DATE, agreement VARCHAR(3))""")
            self.conn.commit()
        except mysql.connector.Error as error:
            wx.MessageBox('Erro', f'Erro ao criar tabela no banco de dados: {error}', wx.OK | wx.ICON_ERROR)

    def close_connection(self):
        if self.conn.is_connected():
            self.c.close()
            self.conn.close()


banc = Database()
