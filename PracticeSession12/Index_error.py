try:
    lst = list(map(int, input("enter the list: ").split()))
    idx = int(input("enter the index: "))
    print(lst[idx])
except IndexError:
    print("Index out of range.")
