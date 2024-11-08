# factorial calculation
# N = int(input("enter value : "))
# f = 1
# i = 1
# while i <= N:
#     f *= i
#     i += 1
# print("Factorial of is", f)


#using For loop
N = int(input("Enter the number: "))
f = 1
for i in range(1, N + 1):
    f *= i
print("Factorial is", f)