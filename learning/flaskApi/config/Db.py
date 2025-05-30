from config.config import DBCONFIG
import mysql.connector
from config.AbstractDb import AbstractDb

class Db(AbstractDb):

    instance = None

    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host=DBCONFIG['host'],
                user=DBCONFIG['user'],
                password=DBCONFIG['password'],
                database=DBCONFIG['database']
            )
            self.cur = self.con.cursor(dictionary=True)
            print("DB connected!")

        except Exception as e:
            print("error", e) 

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Db()
        return cls.instance
    
    @classmethod
    def createInstance(cls):
        cls.instance = Db()
        return cls.instance
        