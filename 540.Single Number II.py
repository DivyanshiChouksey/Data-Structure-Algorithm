# Single Number II

nums = [2,2,3,2]


def singleNumber(nums):
    ones = 0
    twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

print(singleNumber(nums))