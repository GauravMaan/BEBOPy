my_dict = {'a': 10, 'b': 20, 'c': 30}
key = input("Enter the key to search: ")
if key in my_dict:
    print(f"Value: {my_dict[key]}")
else:
    print("Key not found")