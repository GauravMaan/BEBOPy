#Write a program to simulate a login system. It should check if:
	# •	The entered username matches the stored username and
	# •	The entered password matches the stored password.
name="gaurav"
password="gaurav123"
username=input("enter the username: ")
Pass=input("enter the password: ")
if(username==name and Pass==password):
    print("successful")
else:
    print("fail")