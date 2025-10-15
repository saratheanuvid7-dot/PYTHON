from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class UPI(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI"

methods = [CreditCard(), UPI()]
for m in methods:
    print(m.pay(500))
