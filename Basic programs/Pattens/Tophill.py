n=int(input("enter the number: "))
for i in range (n):
    for s in range (1,n-i):
        print(" ",end=" ")
    for c in range(i):
        print("*",end=" ")
    for c in range(i+1):
        print("*",end=" ")
    print()