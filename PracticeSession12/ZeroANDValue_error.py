try:
    num, divisor = map(int, input().split())
    print(num / divisor)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input, please enter numbers.")