n=int(input("enter the number: "))
for i in range (n):
    for v in range (i):
        print(" ",end=" ")
    for j in range(1,n - i):
        print("*", end=" ")
    for j in range(n -i):
        print("*", end=" ")
    print()