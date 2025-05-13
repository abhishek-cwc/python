from config.config import DBCONFIG
import mysql.connector

class Db:

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
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Db()

        return cls.instance
        