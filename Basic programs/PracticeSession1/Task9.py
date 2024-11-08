# 1.	Ask the user for their first name, last name, and age.
# 2.	Concatenate the first name and last name into a single string.
# 3.	Print a greeting message using the concatenated name and age, using an f-string for formatting.

name=input("Enter your First name :")
name1=input("Enter your last name :")
age=int(input("Enter your age"))
Greeting="Welcome"
print(f"Hello : {name + name1}, Age is : {age}")
