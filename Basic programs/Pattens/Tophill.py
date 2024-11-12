# n=int(input("enter the number: "))
# for i in range (n):
#     for s in range (1,n-i):
#         print(" ",end=" ")
#     for c in range(i):
#         print("*",end=" ")
#     for c in range(i+1):
#         print("*",end=" ")
#     print()

# n = 4
# count = 1
# for i in range(n):
#     for s in range(1, n - i):
#         print("  ", end=" ")
#     for c in range(1, i + 1):
#         print(f"{count:2}", end=" ")
#         count += 1
#     for c in range(i+1):
#         print(f"{count:2}", end=" ")
#         count+=1
#     print()

n = int(input("Enter the number: "))
for i in range(1, n + 1):
    for s in range(1, n - i + 1):
        print(" ", end=" ")
    for c in range(1, i):
        print(c, end=" ")
    for c in range(i, 0, -1):
        print(c, end=" ")
    print()

