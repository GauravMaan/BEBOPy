n = int(input("Enter the number: "))
s1 = ""
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        s1+="fizzBuzz"
    elif i % 3 == 0:
        s1+="Fizz"
    elif i % 5 == 0:
        s1+="Buzz"
    else:
        s1+=str(i)
    s1+=" "
print(s1)
