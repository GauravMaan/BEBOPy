n = tuple(map(int, input("Enter tuple: ").split()))
mini = n[0]
maxi = n[0]
for i in n:
    if i < mini:
        mini = i
    else:
        maxi = i
print("Output:", (mini, maxi))
