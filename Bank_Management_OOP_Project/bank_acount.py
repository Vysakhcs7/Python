class BankAccount:

    def __init__(self,accntName,initialAmount):
     self.name = accntName
     self.balance = initialAmount
     print("Account for " + self.name + " has been created.")
     print(f"Your balance is {self.balance}.\n")

    def getBalance(self):
      print(f"{self.name}'s account balance: {self.balance}\n")
      
    def deposit(self, amount):
      self.balance = self.balance + amount
      print(f"Deposit Complete")
      self.getBalance()

