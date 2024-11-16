age = int(input("Enter your age: "))
if age < 12:
    ticket_price = 5
elif 12 <= age <= 64:
    ticket_price = 12
else:
    ticket_price = 7
print(f"The ticket price is ${ticket_price}")
