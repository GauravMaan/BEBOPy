class BankAccount:
    def __init__(self, holder, balance=0):
        self.account_holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance} Name of Account Holder: {self.account_holder}")

account = BankAccount("Gaurav", 1000)
account.check_balance()
account.deposit(float(input("Enter the deposit: ")))
account.withdraw(float(input("Enter the Withdraw: ")))
account.check_balance()

