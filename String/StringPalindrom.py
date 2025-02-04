# n = input("Enter a string: ")
# if n == n[::-1]:
#     print(f"{n} is a palindrome.")
# else:
#     print(f"{n} is not a palindrome.")

# s = input("Enter the string: ")
# s2 = ""
# for i in s:
#     s2 = i + s2
# if s == s2:
#     print(f"{s} is a palindrome:")
# else:
#     print(f"{s} is not a palindrome:")

def palindrome(string1):
    srg = ""
    for i in string1:
        srg = i + srg
    return srg

string1 = "Nitin"
reversed_string = palindrome(string1)
if string1.lower() == reversed_string.lower():
    print("Palindrome")
else:
    print("Not a palindrome")

