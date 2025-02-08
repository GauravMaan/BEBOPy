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

# for multiple
def find_missing_numbers(nums):
    n = len(nums) + len(set(range(1, len(nums) + 2)) - set(nums))
    full_set = set(range(1, n + 1))
    given_set = set(nums)
    missing_numbers = list(full_set - given_set)
    return sorted(missing_numbers)
nums = [1, 2, 4, 6, 7, 9]
print(find_missing_numbers(nums))