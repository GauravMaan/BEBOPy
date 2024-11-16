age = int(input("Enter your age: "))
time = int(input("Enter the time:"))
if age <= 18:
    price = 10
elif 19 <= age <= 59:
    price = 20
else:  # age >= 60
    price = 15
if time >= 20:
    price *= 0.5
print(f"The ticket price is ${price:.2f}")
