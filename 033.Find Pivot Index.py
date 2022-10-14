# Find Pivot Index
"""
"""
# Time Complexity = O() || Space Complexity = O()

nums = [1,7,3,6,5,6]

def pivotIdx(nums):
    totalSum = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = totalSum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1

print(pivotIdx(nums))