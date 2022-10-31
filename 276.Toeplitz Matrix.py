# Toeplitz Matrix

matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]

# Best Solution
"""
    Here we are directly comparing next diagonal values.
"""
# Time Complexity = O(m*n) || Space Complexity = O(1)


def isToeplitzMatrix1(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


# Effective Solution
"""
    Instead of storing difference and then checking the condition we can optimize it by 
    directly checking difference place value and if not same then return false (early stopping)
    if it is same then store it and then check for next value at the end return True.

"""
# Time Complexity = O(n*m) || Space Complexity = O(n)


def isToeplitzMatrix2(matrix):
    dct = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i - j not in dct:
                dct[i - j] = matrix[i][j]
            else:
                if dct[i - j] != matrix[i][j]:
                    return False
    return True


# Naive Solution
"""
    Create a hashmap of difference of index then store values in array and then compare it 
    return False if values are different otherwise return Ture.
"""
# Time Complexity = O(n*m) || Space Complexity =O(n*m)

from collections import defaultdict


def isToeplitzMatrix3(matrix):
    dct = defaultdict(list)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dct[i - j].append(matrix[i][j])

    for nums in dct.values():
        tmp = nums[0]
        for num in nums[1:]:
            if num != tmp:
                print(False)
    return True


print(isToeplitzMatrix1(matrix))
print(isToeplitzMatrix2(matrix))
print(isToeplitzMatrix3(matrix))
