def binary_search(arr):
    low, high = 0, len(arr) - 1
    target = 70
    while low <= high:
        mid = (low + high) // 2  # Calculate mid index
        if arr[mid] == target:
            return mid  # Return index if target is found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Return -1 if target is not found

# Example usage
arr = [10, 20, 30, 40, 50, 60, 70, 80]

ans = binary_search(arr)

if ans != -1:
    print(f"Element found at index {ans}")
else:
    print(f"Element {target} not found")