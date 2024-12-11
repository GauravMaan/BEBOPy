import math

try:
    num = int(input("enter the value: "))
    if num < 0:
        raise ValueError("Negative input is not allowed.")
    print(math.sqrt(num))
except ValueError as e:
    print(e)
