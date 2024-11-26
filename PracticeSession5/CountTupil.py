my_tuple = tuple(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the element to count: "))
count = 0
for item in my_tuple:
    if item == target:
        count += 1
print(f"The element {target} appears {count} times.")