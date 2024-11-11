n = int(input("enter the number: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        n=n-2
    print(c)
    # print("Fibonacci sequence:")
    # while count < n:
    #     print(a, end=" ")
    #     tem = a + b
    #     a = b
    #     b = tem
    #     count += 1
