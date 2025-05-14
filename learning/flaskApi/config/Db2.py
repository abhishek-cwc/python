from config.config import DBCONFIG2
import mysql.connector
from config.AbstractDb import AbstractDb

class Db2(AbstractDb):

    instance = None

    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host=DBCONFIG2['host'],
                user=DBCONFIG2['user'],
                password=DBCONFIG2['password'],
                database=DBCONFIG2['database']
            )
            self.cur = self.con.cursor(dictionary=True)
            print("DB2 connected!")

        except Exception as e:
            print("error", e) 

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Db2()
        return cls.instance
    
    @classmethod
    def createInstance(cls):
        cls.instance = Db2()
        return cls.instance
        