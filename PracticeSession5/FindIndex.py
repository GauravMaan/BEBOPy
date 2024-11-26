numbers = [1, 2, 3, 2, 5, 2]
target = int(input("Enter the Target: "))
indices = []
for i in range(len(numbers)):
    if numbers[i] == target:
        indices.append(i)
result = indices if indices else None
print("Indices:", result)