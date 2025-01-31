arr = [1, 2, 3, 4, 5, 7]
target = 3
found = False  

for i in range(len(arr)):
    if arr[i] == target:
        print(i) 
        found = True 

if not found: 
    print(-1)