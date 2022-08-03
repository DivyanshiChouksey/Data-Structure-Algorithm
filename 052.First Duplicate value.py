# First Duplicate value
array = [8, 1, 5, 2, 9, 12, 9, 6, 9, 9, 5, 13, 5, 9]

# Naive Solution
"""
    For naive solution we can go through array and add them in an empty set and
    return element if we get the duplicate value.
"""
# Time Complexity = O(n) || Space Complexity = O(n)
def firstDuplicateValue(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1


# Optimized Solution
"""
    Basically we are using values and index and checking for negative value if found that means we found a duplicate that is 
    we will go through the array and check if absolute value of element - 1 = index value of array is a negative number or not 
    if it is not a negative number then update the value to a negative number (ie multiply it with -1) 
    otherwise it is a repeated value or we can say a duplicate value so will return the value.
"""
# Time Complexity = O(n) || Space Complexity = O(1)
def firstDuplicateValue1(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


print(firstDuplicateValue(array))
print(firstDuplicateValue1(array))
