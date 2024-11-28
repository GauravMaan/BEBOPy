def palindrome(n):
    if n==n[::-1]:
        print("it is palindrome")
    else:
        print("it is not palindrome")
name=input("enter the string: ")
palindrome(name)
