def binary(arr,target):
    low,high=0 , len(arr) -1
    while low<=high:
        mid=(low+high) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[10,20,30,40,50,60,70,80]
target=70
ans=binary(arr,target)
if ans != -1:
    print(f"Element {target} found at index {ans}")
else:
    print(f"Element {target} not found")
