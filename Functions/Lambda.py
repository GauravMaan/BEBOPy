#a function which has no name
#also called anonymous function
# use with filter(),map(),sorted() function

# x=lambda a:a+10
# print(x(5))
#
# y=lambda a,b:a*b
# print(y(10,20))
#
# z=lambda a,b,c:a*b+c
# print(z(10,20,5))
#

city=["baltan","haryana","panchkula","goa"]
city1=sorted(city, key=lambda x:len(x))
print(city1)

