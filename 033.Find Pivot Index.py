# Find Pivot Index

"""
    Start with taking totalSum and a leftsum initially zero
    then iterate throgh the array, and for every current value
    the rightSum would be substract leftSum and current value from total Sum 
    and check rightSum and leftSum are equal then return current value index else add current value to 
    leftSum after that again do the same step for next value
    and at the end if leftSum is not equal to rightSum then return -1
"""
# Time Complexity = O(n) || Space Complexity = O(1)

nums = [1, 7, 3, 6, 5, 6]


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
