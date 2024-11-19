list = list(input("enter the list:"))
list1 = []
for i in list:
    duplicate = False
    for j in list1:
        if i == j:
            duplicate = True
            break
    if not duplicate:
        list1.append(i)
print("List without duplicates:", list1)