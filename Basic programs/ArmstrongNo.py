number = int(input("Enter a number: "))
num = len(str(number))
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** num
    temp //= 10
if sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
