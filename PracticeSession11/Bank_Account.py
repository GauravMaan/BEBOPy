class BankAccount:
    def __init__(self, acc_number, balance=0):
        self.__acc_number = acc_number
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def get_acc_no(self):
        return self.__acc_number


account = BankAccount("1984345676", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account Number: {account.get_acc_no()}")
print(f"Balance: {account.get_balance()}")