try:
    num, divisor = map(int, input("Enter the numbers: ").split())
    print(num / divisor)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Execution completed, exiting program.")