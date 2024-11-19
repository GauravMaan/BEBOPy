# list0=[1,2,3,4,5,6]
# for i in list0:
#     print(i)

# list1=["apple","mango","banana"]
# print(list1)
# print(list1[0])
# print(list1[-1])
# print(list1[0:1])
# list1[0]="orange"
# print(list1)

# list2=[1,2,3,"apple",234]
# print(list2)

# list3=list()
# print(list3)


# mylist=[1,2,3,4,5,6]
# i=int(input("enter the number: "))
# if i in mylist:
#     print("yes")
# else:
#     print("No")

# mylist=[1,2,3,4,5,6]
# i=int(input("enter the number: "))
# if i not in mylist:
#     print("yes")
# else:
#     print("No")

# mylist=[1,2,3,4,5,6]
# print(len(mylist))

# print("append is use to add the value at the last of the list")
# mylist=[1,2,3,4,5,6]
# mylist.append(3)
# print(mylist)

# print("insert use to add value at specific index")
# mylist=[1,2,3,4,5,6]
# mylist.insert(3,3)
# print(mylist)

# print("pop is to delete the value by providing the index of that value")
# mylist=[1,2,3,3,4,5,6]
# mylist.pop(3)
# print(mylist)

# print("delete is use to delete value as well as list")
# mylist=[1,2,3,3,4,5,6]
# del(mylist)
# print(mylist)

##Copy the list
# mylist=[1,2,3,4,5]
# elist=list(mylist)
# print(mylist)
# print(elist)
# print("<------------>")
# mylist=[1,2,3,4,5]
# elist=[]
# mylist1=mylist.copy()
# print(mylist)
# print(mylist1)

##extend oprater
# list11 = [1, 2, 3]
# list21 = [4, 5, 6]
#
# list11.extend(list21)  # Add elements of list2 to list1
# print(list11)

##append
# my_list101 = [1, 2, 3]
# my_list101.append(4)
# print(my_list101)


# a=input("enter the string: ").split(" ")
# print(a)

a = list(map(int, input("Enter the numbers: ").split()))
print(a)
print("<--------------------------->")
a.sort()
print("after the sort",a)
print("<--------------------------->")
a.sort(reverse=True)
print("After reverse",a)
print("<--------------------------->")
print(a.count(3))








