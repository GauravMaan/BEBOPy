
b = int(input("Enter the base: "))
e = int(input("Enter the exponent: "))
ans = 1
for _ in range(abs(e)):
    ans *= b
if e < 0:
    ans = 1 / ans
print(f"{b} raised to the power of {e} is {ans}")
