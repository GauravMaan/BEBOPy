def find_index(arr):
    target = 3
    for i in range(len(arr)):  # Iterate through the list
        if arr[i] == target:
            return i  # Return index if target is found
    return -1  # Return -1 if target is not found

# Example usage
arr = [1, 2, 3, 4, 5, 7]
print(find_index(arr))  # Output: 2