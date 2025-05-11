from model.resource.Customer import Customer as CustomerResource
class Customer():
    def getCustomerCollection(self):
        result = CustomerResource().getAllCustomer()
        return {'payload':result}
    
    def getCustomerByEmail(self, email: str):
        result = CustomerResource().getCustomerByEmail(email)
        return {'payload':result}