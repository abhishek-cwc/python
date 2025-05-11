from model.resource.Customer import Customer as CustomerResource
class Customer():
    def getCustomerCollection(self):
        result = CustomerResource().getAllCustomer()
        return {'payload':result}