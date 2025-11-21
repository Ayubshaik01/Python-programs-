
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current Balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Current Balance = {self.balance}")

    def show_balance(self):
        print("Final Balance =", self.balance)


acc = BankAccount("Ayub", 1000)
acc.deposit(500)
acc.withdraw(800)
acc.show_balance()
