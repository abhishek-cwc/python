#import mysql.connector
from config.config import DBCONFIG
from config.Db import Db
from config.Service import Service
from config.Db2 import Db2

class Customer():

    def __init__(self, db = Db):
        self.db = Service().get(db)
        self.cur = self.db.cur

    def getAllCustomer(self):
        try:
            self.cur.execute("SELECT * FROM Customer")
            data = self.cur.fetchall()
            return data
        except Exception as e:
            print("Error fetching data:", e)
            return []


    def getCustomerByEmail(self, email: str):
        try:
            #self.cur.execute("SELECT * FROM Customer WHERE email = %s", (email,))
            self.cur.execute(f"SELECT * FROM Customer WHERE email = '{email}'")
            data = self.cur.fetchone()
            return data
        except Exception as e:
            print("Error fetching data:", e)
            return []


    def createCustomer(self, data):
        try:
            sql = "INSERT INTO Customer (name, email, password) VALUES (%s, %s, %s)"
            result = self.cur.execute(sql, (data['name'], data['email'], data['password']))
            self.con.commit()
            last_id = self.cur.lastrowid
            return last_id
        except Exception as e:
            return str(e)
    
    def isCustomerExist(self, data):
        print(data['email'])
        self.cur.execute("select * from Customer where email=%s and password = %s", (data['email'], data['password']))
        result = self.cur.fetchone()
        return result

           