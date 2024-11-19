
nums = tuple(map(int, input("Enter tuple: ").split()))
mini = nums[0]
max = nums[0]
for num in nums:
    if num < mini:
        mini = num
    else:
        max = num
result = (mini, max)
print("Output:", result)
