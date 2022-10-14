# Shortest Unsorted Continuous Subarray
"""
"""
# Time Complexity = O(n) || Space Complexity = O(1)

nums = [2, 6, 4, 8, 10, 9, 15]


# Solution
def findUnsortedSubarray(nums):
    if len(nums) == 1:
        print(0)

    def outOfOrder(i, nums):
        if i == 0:
            return nums[0] > nums[1]
        if i == len(nums) - 1:
            return nums[i] < nums[i - 1]
        return nums[i] > nums[i + 1] or nums[i] < nums[i - 1]

    maxVal = float("-inf")
    minVal = float("inf")

    for i in range(len(nums)):
        if outOfOrder(i, nums):
            maxVal = max(maxVal, nums[i])
            minVal = min(minVal, nums[i])

    if minVal == float("inf"):
        return 0

    i = 0
    while minVal >= nums[i]:
        i += 1

    j = len(nums) - 1
    while maxVal <= nums[j]:
        j -= 1

    if i == j:
        return 0

    return j - i + 1


print(findUnsortedSubarray(nums))


# Time Complexity = O(n) || Space Complexity = O(n)
# Solution
def findUnsortedSubarray1(nums):
    left = right = float("inf")
    temp = sorted(nums)
    for i in range(len(nums)):
        if temp[i] != nums[i]:
            left = i
            break
    if left == float("inf"):
        # return 0
        pass
    for i in reversed(range(len(nums))):
        if temp[i] != nums[i]:
            right = i
            break
    return right - left + 1


print(findUnsortedSubarray1(nums))
