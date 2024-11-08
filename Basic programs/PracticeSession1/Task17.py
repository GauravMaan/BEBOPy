#Write a program that checks if a student is eligible for admission to a specific course. The criteria for eligibility are:
	# •	The student must have scored at least 80% in math and 70% in science.
	# •	Or they must have a total average score of at least 75%.

mat=float(input("Enter the math mask"))
sci=float(input("Enter the sci mask"))
per=mat*100/100
per1=sci*100/100
avg=per+per1/2
if(per>=80 and per1>=70):
    print("eligible for admission")
else:
    print("not eligible")