# Set Mismatch

nums = [1, 2, 2, 4]


def findErrorNums(nums):
    return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]


print(findErrorNums(nums))
