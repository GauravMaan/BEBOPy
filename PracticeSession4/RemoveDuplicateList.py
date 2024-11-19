# list = list(input("enter the list:"))
# list1 = []
# for i in list:
#     duplicate = False
#     for j in list1:
#         if i == j:
#             duplicate = True
#             break
#     if not duplicate:
#         list1.append(i)
# print("List without duplicates:", list1)

list = [1, 1, 2, 3, 4, 5]
i = 0
while i < len(list):
    j = i + 1
    while j < len(list):
        if list[i] == list[j]:
            list.pop(j)
        else:
            j += 1
    i += 1
print(list)
