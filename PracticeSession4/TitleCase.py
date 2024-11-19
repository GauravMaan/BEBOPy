# s = input("Enter a string: ")
# ans = s.title()
# print("Title case string:", ans)

s = input("Enter a string: ")
s1 = ""
ans = True
for i in s:
    if i.isspace():
        s1 += i
        ans = True
    elif ans:
        s1 += i.upper()
        ans = False
    else:
        s1 += i.lower()
print("Title Case:", s1)
