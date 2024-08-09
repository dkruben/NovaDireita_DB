# -*- coding: utf-8 -*-
import os
import sqlite3

import wx

from constants import db_name


class Database:
    def __init__(self):
        self.database = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Nova Direita', 'database', f'{db_name}.db')
        os.makedirs(os.path.dirname(self.database), exist_ok=True)
        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.c = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as error:
            wx.MessageBox('Erro', f'Erro ao conectar ao banco de dados: {error}', wx.OK | wx.ICON_ERROR)

    def create_table(self):
        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS militantes (militant INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT, district TEXT, city TEXT, parish TEXT, zip_code TEXT, phone TEXT, bi_cc TEXT, nif TEXT, email TEXT, birthday DATE, agreement TEXT)""")
            self.conn.commit()
        except sqlite3.Error as error:
            wx.MessageBox('Erro', f'Erro ao criar tabela no banco de dados: {error}', wx.OK | wx.ICON_ERROR)

    def close_connection(self):
        if self.conn:
            self.c.close()
            self.conn.close()


banc = Database()
