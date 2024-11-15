s = input("Enter the string: ")
s1 = {}
for i in s:
    if i in s1:
        s1[i] += 1
    else:
        s1[i] = 1
print(s1)
