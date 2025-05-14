from app import app
from flask import request, make_response, g

from model.Customer import Customer as CustomerModel
from model.Auth import Auth

@app.route("/getAllCustomer")
def getAllCustomer():
    customer = CustomerModel()
    result = customer.getCustomerCollection()
    return sendResponse(result)

@app.route("/getCustomerByEmail/<email>")
@Auth.auth()
def getCustomerByemail(email):
    print("flask global data: ",g.user)
    customer = CustomerModel()
    result = customer.getCustomerByEmail(email)
    return sendResponse(result)

@app.route("/createCustomer", methods=["POST"])
def createCustomer():
    data = request.form.to_dict()
    if not data:
        data = request.get_json()
    customer = CustomerModel()
    result = customer.createCustomer(data)
    return sendResponse(result)

@app.route("/login", methods=["POST"])
def loginCustomer():
    data = request.form.to_dict()
    if not data:
        data = request.get_json()
    customer = CustomerModel()
    result = customer.login(data)
    return sendResponse(result)

def sendResponse(result):
    result.headers['Access-Control-Allow-Origin'] = "*"
    return result
