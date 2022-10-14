# 1 Binary Search

# Time Complexity = O(logn) || Space Complexity = O(1)

nums = [1, 4, 5, 7, 8, 9]
target = 8


def binarySearch(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print(binarySearch(nums))


# ---------------------------------------------------------------------


# 2 Shifted binary search || search in rotated sorted Array

nums = [1, 3]
target = 3


def search(nums, target):
    def helper(nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    return helper(nums, target, 0, len(nums) - 1)


print(search(nums, target))
# def shiftedBinarySearch(array, target):
#         return shiftedBinarySearchHelper(array, target, 0, len(array)-1)


#     def shiftedBinarySearchHelper(array, target, left, right):
#         while left <= right:
#             middle = (left+right)//2
#             potentialMatch = array[middle]
#             leftNum = array[left]
#             rightNum = array[right]
#             if target == potentialMatch:
#                 return middle
#             if leftNum <= potentialMatch:
#                 if target < potentialMatch and target >= leftNum:
#                     right = middle-1
#                 else:
#                     left = middle+1
#             else:
#                 if target > potentialMatch and target <= rightNum:
#                     left = middle+1
#                 else:
#                     right = middle-1
#         return -1


# -------------------------------------------------------------------

# 3 search in sorted matrix || search in 2d matrix

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3


def sortedMatrix(matrix, target):
    i = len(matrix) - 1
    j = 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1
    return False


print(sortedMatrix(matrix, target))

# ----------------------------------------------------------------------

# 4 Find Three Largest Number

array = [55, 7, 8, 3, 43, 11]


def findThreeLargestNumbers(array):
    threeLargest = [float("-inf"), float("-inf"), float("-inf")]
    for num in array:
        if num > threeLargest[2]:
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = threeLargest[2]
            threeLargest[2] = num
        elif num > threeLargest[1]:
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = num
        elif num > threeLargest[0]:
            threeLargest[0] = num
        else:
            continue
    return threeLargest


print(findThreeLargestNumbers(array))


# -------------------------------------------------------------------

# 5 search a range

nums = [1,4,7,8,8,8,9]
target = 8

def searchRange(nums):
    l = 0
    r = len(nums)-1
    i = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            i = mid
            if left


