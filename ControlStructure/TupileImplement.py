# Defining a tuple
tuple = (1, 2, 3, 4, 5)
# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
#Accessing Tuple
print(tuple[0])
print(mixed_tuple[1])
print("<---------------------------------------->")

print(tuple[1:4])
print("<---------------------------------------->")
# Counting occurrences of a value
print(tuple.count(3))
print("<---------------------------------------->")
# Finding the index of a value
print(tuple.index(4))
print("<---------------------------------------->")
a, b, c, d, e = tuple
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

tuple[0] = 10  # This will raise a TypeError