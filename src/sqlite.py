import sqlite3
from datetime import datetime

class Sqlite:

    def __init__(self,db = 'SIP'):
        self.__con = sqlite3.connect(db)
        self.__cur = self.__con.cursor()

    def create_table(self,table = 'data'):
        self.__cur.execute('''CREATE TABLE ? 
                           (id INT PRIMARY KEY, createdate DATE, chanel INT)''',table)
        self.__con.commit()

    def insert_table(self,chanel,datetime = datetime.now(), table = 'data'):
        self.__cur.execute('INSERT INTO ? VALUES(rowid,?,?)',table,datetime,chanel)
        self.__con.commit()

    def query_chanel(self,chanel, table = 'data'):
        self.__cur.execute('SELECT * FROM ? where chanel = ?',table,chanel)
        return self.__cur.fetchall()
