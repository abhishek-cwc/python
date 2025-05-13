from model.resource.Customer import Customer as CustomerResource
from flask import make_response;
import jwt
from config.config import JWTSECRETKEY

class Customer():
    def getCustomerCollection(self):
        result = CustomerResource().getAllCustomer()
        return make_response({'payload':result}, 200)
    
    def getCustomerByEmail(self, email: str):
        result = CustomerResource().getCustomerByEmail(email)
        result = make_response({'payload':result}, 200)
        return result
    
    def createCustomer(self, data):
        print("createcustomer model")
        result = CustomerResource().createCustomer(data)
        result = make_response({'payload':result}, 200)
        return result 
    
    def login(self, data):
        result = CustomerResource().isCustomerExist(data)
        if  result:
            jwToken = jwt.encode({"payload": result}, JWTSECRETKEY, algorithm="HS256")
            res = make_response({'token':jwToken}, 200)  
        else:
            res = make_response({'payload':"Customer not found. Please check!"}, 200) 

        return res       