def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j]>data[j + 1] :
                data[j],data[j + 1]=data[j + 1],data[j]
data=[1, 2, 1, 2, 3, 4, 3, 2, 1]
print("Unsorted",len( data))
bubble_sort(data)
print("Sorted", data)
