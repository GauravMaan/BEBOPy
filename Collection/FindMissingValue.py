def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
nums = [1, 2, 4, 5, 6]
print(find_missing_number(nums))


def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2

    actual_sum = 0
    for num in nums:
        actual_sum += num

    return expected_sum - actual_sum

nums = [1, 2, 4, 5, 6]
print(find_missing_number(nums))