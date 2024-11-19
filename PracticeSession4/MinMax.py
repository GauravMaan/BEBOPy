n = tuple(map(int, input("Enter tuple: ").split()))
mini = maxi = n[0]
for i in n:
    if i < mini:
        mini = i
    if i > maxi:
        maxi = i
print("Output:", (mini, maxi))
