num = int(input("Enter an integer: "))
while num >= 10:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    num = sum
print(f"The single-digit sum is {num}")

