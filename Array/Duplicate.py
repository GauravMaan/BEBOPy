import array
arr = array.array('i', [1, 1, 2, 3, 4, 5, 6, 6, 6])
result = array.array('i', [])
for i in arr:
    if i not in result:
        result.append(i)
print(result)