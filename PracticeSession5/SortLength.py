my_list = ["apple", "banana", "kiwi", "cherry", "mango"]
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if len(my_list[i]) > len(my_list[j]):
            my_list[i], my_list[j] = my_list[j], my_list[i]
print("Sorted list by length of strings:", my_list)