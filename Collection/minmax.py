My_set = {10, 20, 30, 56, 40}
maxi = float('-inf')
mini = float('inf')
for i in My_set:
    if i > maxi:
         maxi = i
    if i < mini:
         mini = i
My_set.remove(mini)
My_set.remove(maxi)
print(My_set)