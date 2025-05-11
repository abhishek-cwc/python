from app import app
from model.Customer import Customer as CustomerModel

@app.route("/getAllCustomer")
def getAllCustomer():
    customer = CustomerModel()
    result = customer.getCustomerCollection()
    return result