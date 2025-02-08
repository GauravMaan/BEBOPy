def second_largest(nums):
    set1=list(set(nums))
    n=len(nums) < 2
    set1.sort()
    return set1[-2]
nums=[1,2,3,4,5,6,7,7,6,5,4,3]
print(second_largest(nums))