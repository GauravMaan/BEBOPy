n=int(input("enter the number: "))
for i in range (n-1):
    for j in range (1,n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for v in range(i):
        print(" ", end=" ")
    for j in range(1, n - i):
        print("*", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()
# n=5
# count=1
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
# for i in range(n):
#     for v in range(i):
#         print(f"{count:2}", end=" ")
#         count += 1
#     for j in range(n - i):
#         print(f"{count:2}", end=" ")
#         count += 1
#     for j in range(n - i-1):
#         print(f"{count:2}", end=" ")
#         count += 1
#     print()



