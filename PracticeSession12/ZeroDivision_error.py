try:
    a, b = 10,0
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed.")