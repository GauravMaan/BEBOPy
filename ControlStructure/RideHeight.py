height = int(input("Enter your height in inches: "))
adult = input("Is an adult present? (yes/no): ").strip().lower() == "yes"
if height >= 48:
    ride = True
elif 42 <= height <= 47 and adult:
    ride = True
else:
    ride = False
if ride:
    print("You can ride.")
else:
    print("You cannot ride.")
