
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i
print(f"The sum of all even numbers from 1 to {n} is {sum}")