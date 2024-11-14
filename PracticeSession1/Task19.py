#Write a program that checks if a person is eligible to drive. The criteria are:
	# •	The person must be at least 18 years old and have a valid driver's license.
print("Enter your age: ")
age = int(input())
if (age >= 18):
    license = input("Do you have a valid driver's license? (yes/no): ")
    if (license == "yes"):
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are not eligible to drive because you are under 18.")
