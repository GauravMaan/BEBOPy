# n=int(input("enter the number: "))
# count=0
# for i in range(n):
#     for c in range(n):
#         count+=1
#         print("#",end=" ")
#     print()

n=5
count=0
for i in range(n):
    for c in range(n):
        count+=1
        print(f"{count:2}",end=" ")
    print()

