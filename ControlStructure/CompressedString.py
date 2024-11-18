s = input("Enter a string: ")
c = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        c += s[i - 1] + str(count)
        count = 1
c += s[-1] + str(count)
print("Compressed string:", c)