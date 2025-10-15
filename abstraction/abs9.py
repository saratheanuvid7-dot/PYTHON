from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            return f"Withdraw {amount}, Balance Left {self.get_balance() - amount}"
        else:
            return "Insufficient Balance"

acc = SavingsAccount(1000)
print(acc.withdraw(500))
