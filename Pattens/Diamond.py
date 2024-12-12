# n=int(input("enter the number: "))
# for i in range (n-1):
#     for j in range (1,n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for v in range(i):
#         print(" ", end=" ")
#     for j in range(1, n - i):
#         print("*", end=" ")
#     for j in range(n - i):
#         print("*", end=" ")
#     print()


# n = 5
# count = 1
#
# # Upper pyramid
# for i in range(n):
#     for s in range(1, n - i):
#         print("  ", end=" ")  # Print spaces for alignment
#     for c in range(1, i + 2):  # Adjusted loop for correct number of elements
#         print(f"{count:2}", end=" ")  # Print numbers with proper formatting
#         count += 1
#     for c in range(i + 1):
#         print(f"{count:2}", end=" ")
#         count += 1
#     print()
#
# # Lower inverted pyramid
# for i in range(n - 1, -1, -1):
#     for s in range(n - i - 1):
#         print("  ", end=" ")  # Print spaces for alignment
#     for c in range(1, i + 2):
#         print(f"{count:2}", end=" ")
#         count += 1
#     for c in range(i + 1):
#         print(f"{count:2}", end=" ")
#         count += 1
#     print()

n =5
for i in range(n-1):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))
for i in range(n - 1, -1, -1):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))



