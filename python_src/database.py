# -*- coding: utf-8 -*-
import mysql.connector

from loggin_setup import logger


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


banc = DataBase()
