#Write a program that asks for a person's age and checks if they are eligible to vote. The voting age is 18 or above.

print("Enter your age: ")
age=int(input())
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible")