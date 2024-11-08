#Write a program that takes a number as input and checks if it falls within a specified range.
# For example, check if the number is between 10 and 50 (inclusive).
print("Enter the number ")
a = float(input())
if (a >= 10 and a <= 50):
    print("number is inclusive")
else:
    print("number is exclusive")
