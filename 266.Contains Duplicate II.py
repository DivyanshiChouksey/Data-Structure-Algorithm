# Contains Duplicate II

nums = [1, 2, 3, 1, 2, 3]
k = 2

# Best Solution
"""
    Making a hashmap to keep track of indices with their value and if we find that element in dct then check 
    abs(i-j)<=k if yes return True else just update index of that element with the new index and again check the condition
    if not then return False 
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def containsNearbyDuplicate(nums, k):
    dct = {}
    for i, num in enumerate(nums):
        if num in dct:
            if abs(dct[num] - i) <= k:
                return True
        dct[num] = i
    return False


print(containsNearbyDuplicate(nums, k))
