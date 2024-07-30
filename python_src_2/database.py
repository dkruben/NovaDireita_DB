# -*- coding: utf-8 -*-
import mysql.connector
import wx


class Database:
    def __init__(self, host='localhost', user='root', password='', database='militantes'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.connection.cursor()
            self.create_table()
        except mysql.connector.Error as error:
            wx.MessageBox('Erro', f'Erro ao conectar ao banco de dados: {error}', wx.OK | wx.ICON_ERROR)

    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS militantes (militant INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, address VARCHAR(255), parish VARCHAR(100), district VARCHAR(100), city VARCHAR(100), zip_code VARCHAR(10), phone VARCHAR(14), bi_cc VARCHAR(20), nif VARCHAR(9), email VARCHAR(100), birthday DATE, agreement VARCHAR(3))""")
            self.connection.commit()
        except mysql.connector.Error as error:
            wx.MessageBox('Erro', f'Erro ao criar tabela no banco de dados: {error}', wx.OK | wx.ICON_ERROR)

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()


banc = Database()
