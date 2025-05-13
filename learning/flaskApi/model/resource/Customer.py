import mysql.connector

class Customer():

    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",
                database="python"
            )
            self.cur = self.con.cursor(dictionary=True)
            print("DB connected!")

        except Exception as e:
            print("error", e)    

        
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
    

           