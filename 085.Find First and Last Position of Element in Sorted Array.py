# Find First and Last Position of Element in Sorted Array
"""
    To check that the target exist in our array we use binary search cause it will take O(logn) time
    and if we have found the given target then from there use shifted binary search(nested binary search) 
    by shifting my mid once to left and once to right to find the starting and ending position of target 
    and this can be achieve in O(logn) runtime.
"""
nums = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 10]
target = 8

# Naive Solution
# Time Complexity = O(n) || Space Complexity = O(1)
def searchRange1(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            break

    if nums[i] != target:  # if number not exists
        return [-1, -1]

    for j in reversed(range(len(nums))):
        if nums[j] == target:
            break

    return [i, j]


# Required Solution
# Time Complexity = O(logn) || Space Complexity = O(1)
def searchRange2(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    if nums[mid] != target:  # if number not exists
        return [-1, -1]

    # left l,
    tmp = mid
    left = l
    right = tmp
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid - 1
        else:
            left = mid + 1
    l = left

    # right ,
    left = mid
    right = r
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        else:
            right = mid - 1

    return [l, right]


print(searchRange1(nums, target))
print(searchRange2(nums, target))
