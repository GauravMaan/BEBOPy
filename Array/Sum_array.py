import array
from functools import reduce

arr = array.array('i', [1, 1, 2, 3, 4, 5, 6, 6, 6])
ans=reduce(lambda x,y:x+y,arr)
print(ans)