try:
    try:
        a, b = map(int, input("Enter the value: ").split())
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        lst = [10, 20, 30]
        idx = int(input("Enter the index: "))
        print(lst[idx])
except IndexError:
    print("Index out of range.")
