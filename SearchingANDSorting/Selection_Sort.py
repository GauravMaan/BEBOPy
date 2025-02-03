def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

data = [64, 25, 12, 22, 11]
selection_sort(data)
print("Selection Sorted Array:", data)