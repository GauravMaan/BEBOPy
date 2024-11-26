numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the number to remove: "))
while target in numbers:
    numbers.remove(target)
print("Modified list:", numbers)