# Search Insert Position
"""
    Simply do binary search and find the insert position
"""
# Time Complexity = O(logn) || Space Complexity = O(1)

nums = [1, 3, 5, 6]
target = 5


def searchPosition(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if nums[mid] > target:
        return mid
    else:
        return mid + 1


print(searchPosition(nums, target))
