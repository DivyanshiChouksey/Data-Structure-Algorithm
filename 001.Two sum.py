# Two Sum
nums = [2, 7, 11, 15]
target = 9


# Naive solution
"""
    using a nested loop and going to every element and checking the sum
"""
# Time Complexity = O(n^2) || Space Complexity = O(1)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Best Solution
"""
    we are using hashmap ,starting with an empty hashmap
    if our target = 7, nums = [2,4,1,5,6,3],
    then loop in array store target - num = index of num if we find number in our hashmap then return both indexes 
"""
# Time Complexity = O(n) || Space Complexity = O(n)
def twoSum2(nums, target):
    dct = {}
    for i, num in enumerate(nums):
        if num in dct:
            return [dct[num], i]
        else:
            dct[target - num] = i


print(twoSum(nums, target))
print(twoSum2(nums, target))
