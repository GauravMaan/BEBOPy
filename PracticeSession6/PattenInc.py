def pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
number=int(input("enter the number: "))
pattern(number)