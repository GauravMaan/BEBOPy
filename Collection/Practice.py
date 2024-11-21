# Tuple3=(1,2,3,4,5)
# list=list(Tuple3)
# list[1]="Gaurav"
# list.insert(0,9)
# ans=tuple(list)
# print(ans)

# mydict={"gaurav":45,"vieck":535}
# mydict1={"gaurav":34}
# mydict.update(mydict1)
# print(mydict)

my_set=set(input("enter the set1: "))
my_set1=set(input("enter the set2: "))
print(my_set^my_set1)
ans=my_set.symmetric_difference(my_set1)
print(type(ans))

