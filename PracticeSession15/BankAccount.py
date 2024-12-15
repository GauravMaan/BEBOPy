class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount < 500:
            raise ValueError("Minimum deposit for Savings Account is 500.")
        self.balance += amount
        return self.balance
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount < 1000:
            raise ValueError("Minimum deposit for Current Account is 1000.")
        self.balance += amount
        return self.balance
savings = SavingsAccount(1000)
current = CurrentAccount(2000)
print(savings.deposit(500))
print(current.deposit(1000))