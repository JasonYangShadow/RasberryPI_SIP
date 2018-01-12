import sqlite3
from datetime import datetime

class Sqlite:

    def __init__(self,db = 'SIP'):
        self.__con = sqlite3.connect(db,isolation_level = None)
        self.__cur = self.__con.cursor()

    def create_table(self,table):
        self.__cur.execute('CREATE TABLE '+table+' (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATE, chanel INTEGER)')

    def drop_table(self,table):
        self.__cur.execute('DROP TABLE '+table)


    def insert_table(self, chanel, table, datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.__cur.execute('INSERT INTO '+table+' VALUES(?,?,?)',(None,datetime,chanel))

    def query_all(self,table):
        self.__cur.execute('SELECT * FROM '+table)
        return self.__cur.fetchall()

    def query_bytime(self,table):
        self.__cur.execute("SELECT * FROM "+table+" WHERE timestamp >= date('now','-1 days')")
        return self.__cur.fetchall()


    def query_chanel(self, chanel, table):
        self.__cur.execute('SELECT * FROM '+table+' where chanel = ?',(chanel,))
        return self.__cur.fetchall()

    def query_delete(self,table):
       self.__cur.execute('SELECT * FROM '+table)
       rows = self.__cur.fetchall()
       self.__cur.execute('DELETE FROM '+table)
       return rows

if __name__ == '__main__':
    sqlite = Sqlite() 
    sqlite.drop_table('hist_data')
    sqlite.drop_table('real_data')
    sqlite.create_table(table = 'hist_data')
    sqlite.create_table(table = 'real_data')
    sqlite.insert_table(12,table = 'real_data')
    print(sqlite.query_delete('real_data'))
    print(sqlite.query_chanel(12,'real_data'))
