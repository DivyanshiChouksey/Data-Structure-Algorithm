# Sort an Array

"""
    Using Merge Sort
"""

# Time Complexity = O(nlogn) || Space Complexity = O(nlogn)


nums = [5, 2, 3, 1]


def sortArray(nums):
    def helper(left, right):
        sortedArray = [None] * (len(left) + len(right))
        k = i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sortedArray[k] = left[i]
                i += 1
            else:
                sortedArray[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sortedArray[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            sortedArray[k] = right[j]
            j += 1
            k += 1
        return sortedArray

    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return helper(sortArray(left), sortArray(right))


print(sortArray(nums))
