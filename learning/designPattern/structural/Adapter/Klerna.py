from Api.Klerna import Klerna as KlernaApiObj
from Gateway.PaymentGateWay import PaymentGateWay

class Klerna(PaymentGateWay):

    def __init__(self, obj: KlernaApiObj):
        self.klernaApi = obj 

    def pay(self):
        print("In Klerna Adapter")
        self.klernaApi.chargePayment()