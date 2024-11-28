def digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    n = sum
    print(f"The single-digit sum is {n}")
num=int(input("enter the number: "))
digit(num)


