from abc import ABC, abstractmethod

class PaymentGateWay:

    @abstractmethod
    def pay(self):
        pass