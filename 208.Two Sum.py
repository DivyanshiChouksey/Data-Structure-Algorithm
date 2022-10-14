# Two Sum
nums = [2, 7, 11, 15]
target = 9


def twoSum3(nums, target):
    dct = {}
    for i, num in enumerate(nums):
        if num in dct:
            return [dct[num], i]
        else:
            dct[target - num] = i


print(twoSum3(nums, target))
