from Api.PayPal import PayPal
from Api.Klerna import Klerna
from Adapter.PayPal import PayPal as PayPalAdapter
from Adapter.Klerna import Klerna as KlernaAdapter

class Client:

    def __init__(self, obj):
        self.gateway = obj

    def pay(self):
        print("Payment through client")
        self.gateway.pay()


#################### Run Code ######################

paypal = PayPal()
payPalAdapter = PayPalAdapter(paypal)

client = Client(payPalAdapter)
client.pay()

klerna = Klerna()
klernaAdapter = KlernaAdapter(klerna)
client = Client(klernaAdapter)
client.pay()

