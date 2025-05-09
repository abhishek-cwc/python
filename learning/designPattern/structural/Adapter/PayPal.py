from Api.PayPal import PayPal as PayPalApiObj
from Gateway.PaymentGateWay import PaymentGateWay

class PayPal(PaymentGateWay):

    def __init__(self, obj: PayPalApiObj):
        self.payPalApi = obj

    def pay(self):
        print("In PayPal Adapter")
        self.payPalApi.makePaymet()