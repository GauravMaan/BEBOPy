# n = input("Enter a string: ")
# if n == n[::-1]:
#     print(f"{n} is a palindrome.")
# else:
#     print(f"{n} is not a palindrome.")

s = input("Enter the string: ")
s2 = ""
for i in s:
    s2 = i + s2
if s == s2:
    print("It is a palindrome:", s)
else:
    print("It is not a palindrome:", s)

