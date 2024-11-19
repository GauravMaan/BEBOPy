# set is unordered collection it does not support the indexing,set is mutable, but values are immutable

my_set={1,2,2,3}
print(my_set)
print("---------------------------")
my_set1={1,4,(2,3)}
# my_set3={1,4,[3,2]}
# print(my_set3)
print(my_set1)
print("---------------------------")
my_set2={1,2,3,4,5}
my_set2.add(6)
print(my_set2)
my_set2.remove(4)#remove throw the error where as discard do not show the error if the value is not in the set
print(my_set2)
my_set2.discard(6)
print(my_set2)
print("---------------------------")
my_set3={1,2,3,4,5,6}
seet={"gaurav","vivekMango"}
my_set3.update(seet)
print(my_set3)
print("---------------------------")
print(my_set|seet)#union
print("---------------------------")
print(my_set2 & my_set3)#intersetion
print("---------------------------")
my_set4={1,2,3,45}
my_set5={1,2,3,4,86}
print(my_set4-my_set5)#difference
print(my_set4^my_set5)#symmetric difference
print("---------------------------")



print("---------------------------")
my_set6={14,2,3,45,5}
fro=frozenset(my_set6)
print(fro)
fro.add(10)
print(fro)

