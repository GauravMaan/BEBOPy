# count the number of digit in a number
a = int(input("Enter the number: "))
count = 0
while a!= 0:
    a=a//10
    count +=1
print("Number of digits:",count)
