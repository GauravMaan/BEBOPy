n=int(input("enter the number: "))
for i in range (n):
    for j in range (1,n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()