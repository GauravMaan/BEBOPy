# list1=[1,2,3,4,5,6,7]
# even_no=list(filter(lambda x:x%2==0,list1))
# print(even_no)


# n=[1,2,3,4]
# sq=list(map(lambda x:x**2,n))
# print(sq)

from functools import reduce
z=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(z)