# reverse of given number
a = int(input("Enter the number: "))
rev = 0
while a != 0:
    rem = a % 10
    rev = rev * 10 + rem
    a = a // 10
print("Reversed number:", rev)