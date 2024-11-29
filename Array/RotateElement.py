import array
arr = array.array('i', [1, 2, 3, 4, 5])
n = int(input("Enter the number of positions to rotate: "))
rotated = arr[n:] + arr[:n]
for i in rotated:
    print(i,end=" ")