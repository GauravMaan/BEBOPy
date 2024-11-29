#array is module in the python, by import array,(array.array(typecode,[elements]),it mutable
#Typecodes
# "i"=signed integer
# "I"=unsigned integer
# "f"=float point number
# "d"=double point
# "u"=uni coded

import array
from os import remove
arr=array.array('i',[1,2,3,45])
for i in arr:
    print(i)
print("-----------------------------------------")
#modifing
arr[1]=10
print(arr)
print("-----------------------------------------")
#adding
arr.append(6)
print(arr)
print("-----------------------------------------")
#remove
arr.remove(6)
print(arr)
print("-----------------------------------------")
#pop for specific element
arr.pop(1)
print(arr)
print("-----------------------------------------")
#extend
arr.extend([6,7])
print(arr)
print("-----------------------------------------")
arr.insert(2,20)
print(arr)
print("-----------------------------------------")
#slice
print(arr[1:3])
print(arr[::2])
print("-----------------------------------------")
#reverse
print(arr[::-1])
print("-----------------------------------------")
#index
arr1=array.array('i',[1,2,3,3,4,5,6])
print(arr1.index(3))
print("-----------------------------------------")
#buffer info
print(arr1.buffer_info())
