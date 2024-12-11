fruits = {"apple": 100, "banana": 30, "mango": 50}
try:
    fruit = input("Enter the fruit: ")
    print(fruits[fruit])
except KeyError:
    print("Fruit not found.")
