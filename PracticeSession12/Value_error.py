# Question 2
try:
    a, b =map(int, input("Enter the value: ").split())
    print(a + b)
except ValueError:
    print("Invalid input, please enter integers.")