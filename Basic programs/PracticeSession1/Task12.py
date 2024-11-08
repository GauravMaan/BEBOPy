#Write a program that takes a student's marks as input and determines the grade based on the following criteria:
	# •	A: Marks greater than or equal to 90
	# •	B: Marks between 80 and 89
	# •	C: Marks between 70 and 79
	# •	D: Marks between 60 and 69
	# •	F: Marks below 60

marks = int(input("Enter the student's marks: "))
if marks >= 90:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: D")
else:
    print("Grade: F")
