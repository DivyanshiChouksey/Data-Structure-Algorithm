# Find Pivot Index

nums = [1, 7, 3, 6, 5, 6]

# Optimal Solution
"""
    Start by storing total sum and iterate through arrayfor the left side remaining sum we subtract prefix and current number
    from total and if it is equal then return index.
"""
# Time Complexity = O(n) || Space Complexity = O(1)
def findPivotIndex(nums):
    total = sum(nums)
    prefix = 0
    for i in range(len(nums)):
        if prefix == (total - nums[i] - prefix):
            return i
        prefix += nums[i]
    return -1


print(findPivotIndex(nums))


# Naive Solution
"""
    Use slicing- slice the nums at each number by for loop and sum the both side and return index if both side is equal.
"""
# Time Complexity = O(n^2) || Space Complexity = O(1)
def findPivotIndex2(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i
    return -1


print(findPivotIndex2(nums))
