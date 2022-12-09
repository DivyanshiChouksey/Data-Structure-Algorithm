# Monotonic Array
"""
    check array is non increasing or non decreasing and
    return true if at least one of them is true
"""
# Time Complexity = O(n) || Space Complexity = O(1)

array = [1, 2, 2, 3]


def isMonotonic(array):
    inc, dec = True, True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            inc = False
        if array[i] < array[i + 1]:
            dec = False
    return inc or dec


print(isMonotonic(array))
