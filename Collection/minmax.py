Myset = {10, 20, 30, 56, 40}
maxi = float('-inf')
mini = float('inf')
for i in Myset:
    if i > maxi:
         maxi = i
    if i < mini:
         mini = i
Myset.remove(mini)
Myset.remove(maxi)
print(Myset)