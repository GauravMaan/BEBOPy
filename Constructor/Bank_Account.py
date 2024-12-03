# class BankAccount:
#     def __init__(self, holder, balance=0):
#         self.account_holder = holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"${amount} deposited successfully.")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"${amount} withdrawn successfully.")
#         elif amount > self.balance:
#             print("Insufficient balance.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#     def check_balance(self):
#         print(f"Current balance: ${self.balance} Name of Account Holder: {self.account_holder}")
#
# account = BankAccount("Gaurav", 1000)
# account.check_balance()
# account.deposit(float(input("Enter the deposit: ")))
# account.withdraw(float(input("Enter the Withdraw: ")))
# account.check_balance()

class BankAccount:
    def __init__(self):
        self.balance = 100000  # Default balance is smaller for simplicity.

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Balance: {self.balance}")

    def display_balance(self):
        print(f"Balance: {self.balance}")


def main():
    account = BankAccount()

    while True:
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = int(input("Withdraw amount: "))
            account.withdraw(amount)
        elif choice == "2":
            amount = int(input("Deposit amount: "))
            account.deposit(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()