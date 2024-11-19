n = tuple(map(int, input("Enter tuple: ").split()))
mini = n[0]
max = n[0]
for i in n:
    if i < mini:
        mini = i
    else:
        max = i
result = (mini, max)
print("Output:", result)
