my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
target_value = 10
keys_value = [key for key, value in my_dict.items() if value == target_value]
print("Keys with the value", target_value, ":", keys_value)

