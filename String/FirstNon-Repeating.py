string = input("Enter a string: ")
count = {}
for char in string:
    count[char] = count.get(char, 0) + 1
re = None
for char in string:
    if count[char] == 1:
        re = char
        break
if re:
    print(f"The first non-repeating character is '{re}'")
else:
    print("No non-repeating character found")
