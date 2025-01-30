my_list = ["hello"]
char_count = {}

for char in my_list[0]:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)