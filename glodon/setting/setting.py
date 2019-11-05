import sys
import sqlite3
import datetime

class Setting():
    db_name = './glodon/setting/setting.db'
    def __init__(self):
        super().__init__()

    def selectSetting(self,code):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('select * from glodon_setting where code = ?',(code,))
        result = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return result
    
    def insertSetting(self,code,value):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('insert into glodon_setting (code,value,ctime) values (?,?,?)',[code,value,datetime.datetime.now()])
        cursor.close()
        conn.commit()
        conn.close()
    def updateSetting(self,code,value,id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('update glodon_setting set code = ? , value = ? , ctime = ? where id = ?',[code,value,datetime.datetime.now(),id])
        cursor.close()
        conn.commit()
        conn.close()

