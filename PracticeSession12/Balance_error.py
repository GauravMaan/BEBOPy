class Balance(Exception):
    pass
try:
    balance = float(input("Enter balance: "))
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise Balance("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)
except Balance as e:
    print(e)