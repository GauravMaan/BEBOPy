# Defining a tuple
Tuple = (1, 2, 3, 4, 5)
# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
#Accessing Tuple
print(Tuple[0])
print(mixed_tuple[1])
print("<---------------------------------------->")


print(Tuple[1:4])
print("<---------------------------------------->")


# Counting occurrences of a value
print(Tuple.count(3))
print("<---------------------------------------->")


# Finding the index of a value
print(Tuple.index(4))
print("<---------------------------------------->")


a, b, c, d, e = Tuple
print(a)
print(b)
print("<---------------------------------------->")


#tuple with single element
tuple1=(1,)
print(type(tuple1))
print("<---------------------------------------->")


#iteration on tuple
tuple1=(1,2,3,4,4)
for i in tuple1:
    print(i)
print("<---------------------------------------->")
#tuple to list
Tuple3=(1,2,3,4,5)
list=list(Tuple3)
list[1]="Gaurav"
list.insert(0,9)
ans=tuple(list)
print(ans)

print("<---------------------------------------->")
tuple2=(1,2,3,2,1)
del(tuple2)
print(tuple2)
print("<---------------------------------------->")

tuple[0] = 10  # This will raise a TypeError
