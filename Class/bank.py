# Encapsulation: Public, Private, Protected
class BankAccount:
    def __init__(self, account_number, balance=0):
        # Protected variable
        self._account_number = account_number  
        # Private variable
        self.__balance = balance               

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} into Account {self._account_number}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from Account {self._account_number}. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Inheritance
# Savings Account Class (Inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate, balance=0):
        super().__init__(account_number, balance)
        # Protected variable
        self._interest_rate = interest_rate  

    def add_interest(self):
        interest = self.get_balance() * (self._interest_rate / 100)
        self.deposit(interest)
        print(f"Interest added to Account {self._account_number}. New balance: {self.get_balance()}")


# Current Account Class (Inherits from BankAccount)
class CurrentAccount(BankAccount):
    def __init__(self, account_number, overdraft_limit, balance=0):
        super().__init__(account_number, balance)
        # Private variable
        self.__overdraft_limit = overdraft_limit  

    def withdraw(self, amount):
        if amount <= (self.get_balance() + self.__overdraft_limit):
            # Accessing protected variable directly
            print(f"Withdrew {amount} from Account {self._account_number}. New balance: {self.get_balance()}")
            self._BankAccount__balance -= amount
        else:
            print("Exceeded overdraft limit")


# Polymorphism: Method overriding
# CustomAccount Class (Inherits from BankAccount)
class CustomAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    # Method overriding
    def deposit(self, amount):
        self._BankAccount__balance += amount
        print(f"Deposited {amount} into Custom Account {self._account_number}. New balance: {self.get_balance()}")


# Abstraction: Abstract class
from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass


# Main program
if __name__ == "__main__":
    # Create bank accounts
    savings_acc = SavingsAccount("SAV001", 5, 1000)
    current_acc = CurrentAccount("CUR001", 500, 2000)
    custom_acc = CustomAccount("CUS001", 3000)

    # Perform transactions
    print("Initial Account Details:")
    print(savings_acc.get_balance())
    print(current_acc.get_balance())
    print(custom_acc.get_balance())

    savings_acc.deposit(500)
    savings_acc.add_interest()
    savings_acc.withdraw(200)
    print()

    current_acc.deposit(1000)
    current_acc.withdraw(2500)
    print()

    custom_acc.deposit(700)
    custom_acc.withdraw(200)
