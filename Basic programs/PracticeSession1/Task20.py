# Write a program that takes two values from the user. Check if:
# 	•	Both values are positive or if both values are negative.
# 	•	If they are mixed (one positive and one negative), print "Mixed signs".
print("enter the first number: ")
a=int(input())
print("enter the second number: ")
b=int(input())
if(a > 0 and b > 0):
    print("Both values are positive")
elif(a < 0 and b < 0):
    print("both values are negative")
else:
    print("one positive and one negative")