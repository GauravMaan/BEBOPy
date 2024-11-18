list = list(input("enter the list:"))
list1 = []
for item in list:
    duplicate = False
    for Unitem in list1:
        if item == Unitem:
            duplicate = True
            break
    if not duplicate:
        list1.append(item)

print("List without duplicates:", list1)