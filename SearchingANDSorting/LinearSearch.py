def find_index(arr, target):
    for i in range(len(arr)):  # Iterate through the list
        if arr[i] == target:
            return i  # Return index if target is found
    return -1  # Return -1 if target is not found

# Example usage
arr = [1, 2, 3, 4, 5, 7]
target = 3
print(find_index(arr, target))  # Output: 2