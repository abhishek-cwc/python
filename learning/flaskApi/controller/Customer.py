from app import app
from flask import request
from model.Customer import Customer as CustomerModel

@app.route("/getAllCustomer")
def getAllCustomer():
    customer = CustomerModel()
    result = customer.getCustomerCollection()
    return result

@app.route("/getCustomerByEmail/<email>")
def getCustomerByemail(email):
    customer = CustomerModel()
    result = customer.getCustomerByEmail(email)
    print(result)
    return result