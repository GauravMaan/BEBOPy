# n=int(input("enter the number: "))
# count=0
# for i in range(n):
#     for c in range(n):
#         count+=1
#         print("#",end=" ")
#     print()

# n=5
# count=0
# for i in range(n):
#     for c in range(n):
#         count+=1
#         print(f"{count:2}",end=" ")
#     print()

n = int(input("Enter the number: "))

for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()
