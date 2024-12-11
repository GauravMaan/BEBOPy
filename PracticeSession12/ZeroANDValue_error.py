try:
    num, divisor = map(int, input("enter the numbers: ").split())
    print(num / divisor)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input, please enter numbers.")